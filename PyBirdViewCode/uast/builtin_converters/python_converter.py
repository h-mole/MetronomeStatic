from dataclasses import dataclass
from typing import Any, Callable, Dict, Literal, Optional, Union, Type
import warnings
import parso
from parso.tree import NodeOrLeaf
from parso.python.tree import PythonNode, Operator
import parso.python.tree as parso_tree
from PyBirdViewCode.uast import universal_ast_nodes as nodes
from .converter_base import BaseASTExtractor, BaseUASTConverter
import ast
from inspect import isclass


def extract_classes(global_vals: dict) -> dict:
    d = {k for k, v in global_vals.items() if k != "__builtins__" and isclass(v)}
    d.update({k for k, v in global_vals["__builtins__"].items() if isclass(v)})
    return d


class ParsoASTExtractor(BaseASTExtractor):
    @classmethod
    def supported_file_types(cls):
        return [".py", ".pyi"]

    def extract_ast(self) -> tuple[tuple[ast.AST, dict], list[str]]:
        with open(self.file, "r") as f:
            file_content = f.read()
            module: ast.AST = ast.parse(file_content)
            globals_to_exec = {}
            exec(file_content, globals_to_exec)
            # import pdb;pdb.set_trace()
            return (
                module,
                {"classes_names": extract_classes(globals_to_exec)},
            ), []


@dataclass
class VarScope:
    name: str
    kind: Literal["class", "function", "global"]
    variables: dict[str, nodes.DATA_TYPE]


class VarScopeMgr:
    class VarScopeCtxMgr:
        def __init__(self, var_scope_mgr, name, kind) -> None:
            self.var_scope_mgr: VarScopeMgr = var_scope_mgr
            self.kind = kind
            self.name = name

        def __enter__(self):
            self.var_scope_mgr.scopes_stack.append(VarScope(self.name, self.kind, {}))

        def __exit__(self, exc_type, exc_value, traceback):
            self.var_scope_mgr.scopes_stack.pop()

    def __init__(self) -> None:
        self.scopes_stack: list[VarScope] = [VarScope("", "global", {})]

    @property
    def top_scope(self):
        return self.scopes_stack[-1]

    def add_var(self, name: str, type: nodes.DATA_TYPE) -> None:
        self.top_scope.variables[name] = type

    def get_context_manager(
        self, name: str, kind: Literal["class", "function", "global"]
    ):
        """
        :name: 类/函数/方法的名称。如果是方法, 则写C.id
        :kind: 该变量管理的类型
        """
        return VarScopeMgr.VarScopeCtxMgr(self, name, kind)

    def lookup_variable_type(self, name: str) -> Optional[nodes.DATA_TYPE]:
        for scope in reversed(self.scopes_stack):
            if name in scope.variables:
                return scope.variables[name]


class UASTTypeInfer:
    """
    用于推断出UAST中每一个函数或作用域下的变量类型
    """

    def __init__(self, full_uast) -> None:
        # Record the current variable scope
        # The first element records the global scope
        self.scopes = VarScopeMgr()
        self.full_uast: nodes.CompilationUnit = full_uast
        self.method_scopes = {}

    def infer(self, node: nodes.CompilationUnit):
        self._infer_scopes(node)

    def _infer_type(self, node: nodes.SourceElement) -> nodes.DATA_TYPE:
        match node:
            case nodes.InstanceCreationExpr(type=type):
                return nodes.ClassType(type.name)
            case nodes.CallExpr(name=callee):
                callee_type = self._infer_type(callee)
                raise NotImplementedError
            case nodes.FieldAccessExpr(name=name, target=target):
                target_type = self._infer_type(target)
                print(target_type, name)
                match target_type:
                    case nodes.ClassType(name=class_name):
                        cls_uast = self.full_uast.filter_by(
                            nodes.ClassDecl, name=class_name
                        ).head()
                        methods = cls_uast.filter_by(nodes.MethodDecl, name=name).l
                        if len(methods) == 1:
                            method = methods[0]
                            return nodes.MethodType(
                                [
                                    nodes.UnknownType("any")
                                    for arg in method.type.pos_args
                                ],
                                methods[0].type.return_type,
                            )
                        raise NotImplementedError(target)
                    case _:
                        raise NotImplementedError
            case nodes.Name(id=name):
                var_type = self.scopes.lookup_variable_type(name)
                assert var_type is not None, f"variable {name} is not defined"
                return var_type
            case _:
                raise NotImplementedError(node)

    def _infer_list(self, nodes_to_infer: list):
        for stmt in nodes_to_infer:
            self._infer_scopes(stmt)

    def _infer_scopes(self, node: nodes.SourceElement):
        match node:
            case nodes.CompilationUnit():
                self._infer_list(node.children)
            case nodes.BlockStmt():
                self._infer_list(node.statements)
            case nodes.MethodDecl():
                with self.scopes.get_context_manager("function"):
                    self._infer_scopes(node.body)
            case nodes.ClassDecl():
                with self.scopes.get_context_manager("class"):
                    self._infer_scopes(node.body)
            case nodes.Assignment(lhs=lhs, rhs=rhs):
                for lvalue, rvalue in zip(lhs, rhs):
                    if isinstance(lvalue, nodes.Name):
                        self.scopes.add_var(lvalue.id, self._infer_type(rvalue))
            case nodes.CallExpr():
                pass
            case _:
                raise NotImplementedError(node)

    # def _infer_stmts(self, node: nodes.SourceElement):
    #     pass


class ParsoASTConverter(BaseUASTConverter):
    def __init__(self, classes_names: set[str]) -> None:
        # self.source_location_filter: Optional[Callable[[SourceLocation], bool]] = None
        self._handlers_map: Dict[Type, Callable[[NodeOrLeaf], Any]] = {
            ast.Expr: lambda expr: self.eval_single_node(expr.value),
            ast.DictComp: lambda expr: nodes.NotImplementedItem("dictcomp"),
            ast.Assign: self._handle_assignment,
            ast.AnnAssign: self._handle_ann_assign,
            ast.AugAssign: self._handle_aug_assign,
            ast.Call: self._handle_call,
            ast.Assert: lambda stmt: nodes.AssertStmt(
                self.eval_single_node(stmt.test), self.eval_single_node(stmt.msg)
            ),
            ast.Raise: lambda stmt: nodes.ThrowStmt(self.eval_single_node(stmt.exc)),
            ast.JoinedStr: self._handle_joined_str,
            # ast.Is: lambda expr: nodes.BinaryExpr("is", expr),
            # ast.arg: self._handle_arg,
            # "arith_expr": self._handle_arith_expr,
            ast.Name: self._handle_name,
            ast.ClassDef: self._handle_class_def,
            ast.FunctionDef: self._handle_function_def,
            ast.Pass: lambda node: nodes.UnknownType("Pass"),
            ast.Compare: self._handle_compare,
            ast.Constant: self._handle_number,
            ast.BinOp: self._handle_bin_op,
            ast.UnaryOp: self._handle_unary_op,
            # "string": self._handle_string,
            # "expr_stmt": self._handle_expr_stmt,
            # "atom_expr": self._handle_atom_expr,
            ast.Yield: self._handle_yield,
            # "trailer": self._handle_trailer,
            ast.If: self._handle_if_stmt,
            ast.For: self._handle_for_stmt,
            # "funcdef": self._handle_funcdef,
            # "suite": self._handle_suite,
            # # "newline": lambda _: (),
            # "simple_stmt": lambda stmt: self.eval_single_node(stmt.children[0]),
            ast.While: self._handle_while,
            # "atom": self._handle_atom,
            ast.Return: self._handle_return,
            # "keyword": self._handle_keyword,
            ast.Attribute: self._handle_attribute,
            ast.Subscript: self._handle_subscript,
            ast.Module: self._handle_module,
            ast.Import: self._handle_import_name,
            ast.ImportFrom: self._handle_import_from,
            ast.BoolOp: self._handle_bool_op,
            ast.IfExp: self._handle_if_exp,
            ast.Dict: self._handle_dict,
            # "dotted_as_name": self._handle_not_implemented,
            # "atom_expr": self._handle_not_implemented,
        }

        # Return value of execution
        self._ret_value = None
        self.classes = classes_names

    @classmethod
    def supported_ast_types(cls) -> list[Type]:
        """
        返回可以应用的抽象语法树对象类型

        :return: 该UAST转换类支持的所有抽象语法树对象类型
        """
        return [ast.AST]

    def convert_to_uast(self, original_ast: Any) -> nodes.SourceElement:
        """将某个语言的AST转换为UAST"""
        return self.eval(original_ast)

    def _handle_unary_op(self, expr: ast.UnaryOp) -> nodes.UnaryExpr:
        mapping = {ast.Not: ("!", True)}
        op, op_before_expr = mapping[type(expr.op)]
        return nodes.UnaryExpr(op, self.eval_single_node(expr.operand), op_before_expr)

    def _handle_bin_op(self, expr: ast.BinOp) -> nodes.BinaryExpr:
        mapping = {ast.Add: "+", ast.Sub: "-"}
        return nodes.BinaryExpr(
            mapping[type(expr.op)],
            self.eval_single_node(expr.left),
            self.eval_single_node(expr.right),
        )

    def _handle_trailer(self, c: parso_tree.PythonNode) -> nodes.CallExpr:
        raise ValueError(
            "Cannot handle such type. Please handle this type on higher call stack method."
        )

    # def _handle_is(self, expr: ast.Is) -> nodes.Is
    def _handle_call(
        self, call: ast.Call
    ) -> Union[nodes.CallExpr, nodes.InstanceCreationExpr]:
        """
        This method may return calls or instance creations.
        """
        called_func_ast = self.eval_single_node(call.func)
        match called_func_ast:
            case nodes.Name(id=callee_name) if callee_name in self.classes:
                return nodes.InstanceCreationExpr(
                    nodes.ClassType(callee_name),
                    arguments=self.eval_list(call.args),
                )
            case _:
                return nodes.CallExpr(called_func_ast, self.eval_list(call.args))
        # return nodes.CallExpr(called_func_ast, self.eval_list(call.args))

    def _handle_attribute(self, attr: ast.Attribute) -> nodes.FieldAccessExpr:

        return nodes.FieldAccessExpr(attr.attr, self.eval_single_node(attr.value))

    def _handle_subscript(self, node: ast.Subscript) -> nodes.ArrayAccessExpr:
        return nodes.ArrayAccessExpr(
            self.eval_single_node(node.slice), self.eval_single_node(node.value)
        )

    def _handle_aug_assign(self, stmt: ast.AugAssign) -> nodes.Assignment:
        mapping = {ast.Add: "+=", ast.Sub: "-=", ast.Mult: "*=", ast.Div: "/="}
        return nodes.Assignment(
            mapping[type(stmt.op)],
            [self.eval_single_node(stmt.target)],
            [self.eval_single_node(stmt.value)],
        )

    def _handle_ann_assign(self, stmt: ast.AnnAssign) -> nodes.Assignment:
        # match stmt.
        return nodes.Assignment(
            "=",
            [self.eval_single_node(stmt.target)],
            [self.eval_single_node(stmt.value)],
        )

    def _handle_assignment(self, assign: ast.Assign) -> nodes.Assignment:
        expr = None
        for target in reversed(assign.targets):
            target_uast = self.eval_single_node(target)
            if expr is None:
                expr = nodes.Assignment(
                    "=",
                    [target_uast],
                    [self.eval_single_node(assign.value)],
                )
            else:
                expr = nodes.Assignment(
                    "=",
                    [target_uast],
                    [expr],
                )
            # self.scopes.add_var(target_uast, expr)
        return expr

    def _handle_atom_expr(self, c: parso_tree.PythonNode) -> nodes.FieldAccessExpr:
        field_name = c.children[0]
        target = c.children[-1]
        return nodes.FieldAccessExpr(
            self.eval_single_node(field_name), self.eval_single_node(target)
        )

    def _handle_not_implemented(self, c: parso_tree.PythonNode) -> nodes.UnknownType:
        return nodes.UnknownType("Unknown parso type" + c.type)

    def _handle_import_from(self, c: ast.ImportFrom) -> nodes.ImportDecl:
        return nodes.UnknownType("From...import... to be implemented")

    def _handle_import_name(self, c: ast.Import) -> nodes.ImportDecl:
        return nodes.UnknownType("import... to be implemented")
        return nodes.ImportDecl(name=name, path=".")

    def _handle_module(self, c: ast.Module) -> nodes.CompilationUnit:
        return nodes.CompilationUnit([self.eval(child) for child in c.body])

    def _handle_keyword(self, c: parso_tree.ReturnStmt) -> nodes.ReturnStmt:
        if c.value == "return":
            return nodes.ReturnStmt()
        else:
            raise NotImplementedError(c)

    def _handle_return(self, c: ast.Return) -> nodes.Stmt:
        return nodes.ReturnStmt(
            [self.eval_single_node(c.value)] if c.value is not None else [nodes.Null()]
        )

    def _handle_atom(self, c: parso_tree.PythonNode) -> nodes.Expr:
        if len(c.children) == 3:
            match (c.children[0], c.children[2]):
                case (parso_tree.Operator(value="("), parso_tree.Operator(value=")")):
                    return self.eval_single_node(c.children[1])
        raise NotImplementedError

    def _handle_suite(self, c: parso_tree.PythonNode) -> nodes.BlockStmt:

        return nodes.BlockStmt(
            [
                self.eval_single_node(stmt)
                for stmt in c.children
                if stmt.type not in ("newline")
            ]
        )

    # def _handle_funcdef(self, c: parso_tree.Function) -> nodes.MethodDecl:
    #     # param: parso_tree.Param
    #     # param.
    #     method_type = nodes.MethodType(
    #         [
    #             nodes.ParamDecl(
    #                 self.eval_single_node(param.name), nodes.UnknownType("any")
    #             )
    #             for param in c.get_params()
    #         ],
    #         nodes.UnknownType("any"),
    #     )
    #     method_decl = nodes.MethodDecl(
    #         self.eval_single_node(c.name),
    #         method_type,
    #         self.eval_single_node(c.children[-1]),
    #         # c.iter
    #     )
    #     return method_decl

    def _handle_class_def(self, node: ast.ClassDef) -> nodes.ClassDecl:
        return nodes.ClassDecl(node.name, nodes.BlockStmt(self.eval_list(node.body)))

    def _handle_function_def(self, node: ast.FunctionDef) -> nodes.MethodDecl:
        arguments = node.args
        args_list = []
        for arg in arguments.args:
            args_list.append(nodes.ParamDecl(nodes.Name(arg.arg), None))
        return nodes.MethodDecl(
            nodes.Name(node.name),
            nodes.MethodInfo(args_list, nodes.UnknownType("UNKNOWN")),
            nodes.BlockStmt(self.eval_list(node.body)),
            # self.eval_single_node(node.returns) if node.returns is not None else None,
            # self.eval_single_node(node.decorator_list),
        )

    def _handle_name(self, node: ast.Name) -> nodes.Name:
        return nodes.Name(node.id)

    def _handle_joined_str(self, s: ast.JoinedStr) -> nodes.Literal:
        #  "+" (values)
        return nodes.Literal("Notimplemented joined str", "string")

    def _handle_yield(self, node: ast.Yield) -> nodes.Yield:
        return nodes.Yield(self.eval_single_node(node.value))

    def _handle_if_stmt(self, node: ast.If) -> nodes.IfThenElseStmt:
        stmt = nodes.IfThenElseStmt(
            self.eval_single_node(node.test),
            nodes.BlockStmt(self.eval_list(node.body)),
            nodes.BlockStmt(self.eval_list(node.orelse)) if node.orelse else None,
        )
        return stmt

    def _handle_while(self, node: ast.While) -> nodes.WhileStmt:
        return nodes.WhileStmt(
            self.eval_single_node(node.test), nodes.BlockStmt(self.eval_list(node.body))
        )

    def _handle_for_stmt(self, node: ast.For) -> nodes.ForStmt:
        """
        将Python中的for循环转换为类C风格的For循环
        """
        assert node.orelse is None or len(node.orelse) == 0
        iterator_var_name = self.create_temporary_variable_name("iterator_")
        loop_times_counter_name = self.create_temporary_variable_name("counter_")

        # 迭代器初始化语句
        iterator_init_expr = nodes.VarDecl(
            nodes.Name(iterator_var_name), self.eval_single_node(node.iter)
        )
        loop_times_counter = nodes.Name(loop_times_counter_name)
        # 循环计数变量语句
        loop_times_counter_decl = nodes.VarDecl(
            loop_times_counter, nodes.Literal(0, "int")
        )
        target_var_uast = self.eval_single_node(node.target)
        assert isinstance(target_var_uast, nodes.Name)
        target_var_decl = nodes.VarDecl(target_var_uast)
        # for循环前，需要将迭代器的内容赋值给迭代变量
        variable_updates = [
            nodes.Assignment(
                "=",
                [target_var_uast],
                [nodes.CallExpr(nodes.Name("next"), [nodes.Name(iterator_var_name)])],
            ),
            nodes.IfThenElseStmt(
                nodes.BinaryExpr(
                    "==",
                    nodes.Name(iterator_var_name),
                    nodes.Name("StopIteration"),
                ),
                nodes.BlockStmt([nodes.BreakStmt()]),
                None,
            ),
        ]
        # for循环体后，需要判断循环变量是否已经到达了迭代器的末尾
        # variable_checks = [

        # ]
        body_stmts = variable_updates + self.eval_list(node.body)

        return nodes.ForStmt(
            nodes.CompoundDecl(
                [iterator_init_expr, loop_times_counter_decl, target_var_decl]
            ),
            None,
            nodes.Assignment("+=", [loop_times_counter], [nodes.Literal(1, "int")]),
            nodes.BlockStmt(body_stmts),
        )

    def _handle_expr_stmt(self, node: parso_tree.ExprStmt) -> Union[nodes.Expr]:
        if len(node.children) == 2:
            expr: PythonNode
            lhs, expr = node.children
            if expr.type == "annassign":
                op, rhs = expr.children[2:]
                return nodes.Assignment(
                    op.value,
                    [self.eval_single_node(lhs)],
                    [self.eval_single_node(rhs)],
                )
            else:
                raise NotImplementedError(node)
        elif len(node.children) == 3:
            assert node.type == "expr_stmt"
            op: Operator
            lhs, op, rhs = node.children
            return nodes.Assignment(
                op.value, [self.eval_single_node(lhs)], [self.eval_single_node(rhs)]
            )
        else:
            lhs, op, *remaining_children = node.children
            if op.value == "=":
                # 解决一连串赋值的情况，如a=b=123
                return nodes.Assignment(
                    op.value,
                    [self.eval_single_node(lhs)],
                    [self.eval_single_node(PythonNode(node.type, remaining_children))],
                )
            else:
                raise NotImplementedError(op.value)

    def _handle_if_exp(self, node: ast.IfExp) -> nodes.Conditional:
        return nodes.Conditional(
            self.eval_single_node(node.test),
            self.eval_single_node(node.body),
            self.eval_single_node(node.orelse),
        )

    def _handle_dict(self, dic: ast.Dict) -> nodes.CallExpr:
        if len(dic.keys) == 0:
            return nodes.CallExpr(nodes.Name("dict"), [])
        else:
            raise NotImplementedError

    def _handle_bool_op(self, node: ast.BoolOp) -> nodes.BinaryExpr:
        mapping = {ast.Or: "||"}
        expr = None
        for i in range(len(node.values) - 1):
            operand1 = node.values[i]
            operand2 = node.values[i + 1]
            if expr is None:
                expr = nodes.BinaryExpr(
                    mapping[type(node.op)],
                    self.eval_single_node(operand1),
                    self.eval_single_node(operand2),
                )
            else:
                expr = nodes.BinaryExpr(
                    mapping[type(node.op)],
                    expr,
                    self.eval_single_node(operand2),
                )
        return expr

    def _handle_compare(self, node: ast.Compare) -> nodes.BinaryExpr:
        mapping = {
            ast.Lt: "<",
            ast.LtE: "<=",
            ast.Gt: ">",
            ast.GtE: ">=",
            ast.Eq: "==",
            ast.NotEq: "!=",
            ast.Is: "is",
            ast.In: "in",
            # Negative operators are also in this dict
            # but requiring negation
            ast.NotIn: "in",
            ast.IsNot: "is",
        }
        requiring_negation = {ast.NotIn, ast.NotEq}

        match node:
            case ast.Compare(ops=list(), comparators=list()):
                last_comp = node.left
                created_expr = None
                # last_expr = None
                for op, comp in zip(node.ops, node.comparators):
                    # if type(op) in mapping:
                    expr = nodes.BinaryExpr(
                        mapping[type(op)],
                        self.eval_single_node(last_comp),
                        self.eval_single_node(comp),
                    )
                    if type(op) in requiring_negation:
                        expr = nodes.UnaryExpr("!", expr, True)
                    if created_expr is None:
                        created_expr = expr
                    else:
                        created_expr = nodes.BinaryExpr("&&", created_expr, expr)
                    last_comp = comp
                return created_expr
            case _:
                raise NotImplementedError()

    def _handle_number(self, node: ast.Constant) -> nodes.Literal:
        match node.value:
            case int():
                return nodes.Literal(node.value, "int")
            case float():
                return nodes.Literal(node.value, "float")
            case complex():
                return nodes.Literal(node.value, "complex")
            case None:
                return nodes.Null()
            case str():
                return nodes.Literal(node.value, "string")
            case _:
                raise NotImplementedError(node.value)

    def _handle_arith_expr(self, node: PythonNode) -> nodes.BinaryExpr:
        op: Operator
        lval, op, rval = node.children
        return nodes.BinaryExpr(
            op.value,
            self.eval_single_node(lval),
            self.eval_single_node(rval),
        )

    def eval(self, node: NodeOrLeaf) -> nodes.SourceElement:
        return self.eval_single_node(node)

    def eval_single_node(self, node: ast.AST) -> nodes.SourceElement:
        try:
            return self._handlers_map[type(node)](node)
        except KeyError as e:
            warnings.warn(f"node:{ ast.dump(node)}")
            raise ValueError

    def eval_list(self, nodes: list[ast.AST]) -> list[nodes.SourceElement]:
        return [self.eval_single_node(node) for node in nodes]
