from typing import Any, Callable, Dict, Union, Type
import parso
from parso.tree import NodeOrLeaf
from parso.python.tree import PythonNode, Operator
import parso.python.tree as parso_tree
from PyBirdViewCode.uast import universal_ast_nodes as nodes
from .converter_base import BaseASTExtractor, BaseUASTConverter
import ast


class ParsoASTExtractor(BaseASTExtractor):
    @classmethod
    def supported_file_types(cls):
        return [".py", ".pyi"]

    def extract_ast(self) -> tuple[PythonNode, list[str]]:
        with open(self.file, "r") as f:
            module: parso_tree.Module = ast.parse(f.read())
            # print(module.children)
            # print(type(module))
            return module, []


class ParsoASTConverter(BaseUASTConverter):
    def __init__(
        self,
    ) -> None:
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
            # "yield_expr": self._handle_yield_expr,
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
        # self._labels: Dict[str, LabelDesc] = {}

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
    def _handle_call(self, call: ast.Call) -> nodes.CallExpr:
        print(ast.dump(call, indent=4))
        func_ast = self.eval_single_node(call.func)

        return nodes.CallExpr(func_ast, self.eval_list(call.args))

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
        match assign:
            case ast.Assign(value=list()):
                return nodes.Assignment(
                    "=", self.eval_list(assign.targets), self.eval_list(assign.value)
                )
            case ast.Assign():
                return nodes.Assignment(
                    "=",
                    self.eval_list(assign.targets),
                    [self.eval_single_node(assign.value)],
                )
            case _:
                raise NotImplementedError

    def _handle_atom_expr(self, c: parso_tree.PythonNode) -> nodes.FieldAccessExpr:
        print(c.children)
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
        # print(ast.dump(c, indent=2))
        # name = [self.eval_single_node(name) for name in c.names]
        # print(name)
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
        return nodes.ClassDecl(node.name, self.eval_list(node.body))

    def _handle_function_def(self, node: ast.FunctionDef) -> nodes.MethodDecl:
        arguments = node.args
        # print(ast.dump(node))
        # raise NotImplementedError
        args_list = []
        for arg in arguments.args:
            args_list.append(nodes.ParamDecl(nodes.Name(arg.arg), None))
        # self.eval_list()
        # print(node.body)
        print("AAAAA", lst := self.eval_list(node.body))
        print("BBBBB", node.body)
        return nodes.MethodDecl(
            nodes.Name(node.name),
            nodes.MethodType(args_list, nodes.UnknownType("UNKNOWN")),
            nodes.BlockStmt(lst),
            # self.eval_single_node(node.returns) if node.returns is not None else None,
            # self.eval_single_node(node.decorator_list),
        )

    def _handle_name(self, node: ast.Name) -> nodes.Name:
        return nodes.Name(node.id)

    def _handle_joined_str(self, s: ast.JoinedStr) -> nodes.Literal:
        #  "+" (values)
        return nodes.Literal("Notimplemented joined str", "string")

    def _handle_yield_expr(self, node: parso_tree.YieldExpr) -> nodes.Yield:
        _, value = node.children
        return nodes.Yield(self.eval_single_node(value))

    def _handle_if_stmt(self, node: ast.If) -> nodes.IfThenElseStmt:
        # print(node.children)

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

        print(ast.dump(node))
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
            print(
                operand1,
                operand2,
                self.eval_single_node(operand1),
                self.eval_single_node(operand2),
            )
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
            if hasattr(node, "lineno"):
                print("line：", node.lineno)
            print("node:", ast.dump(node))
            # print(e)
            raise ValueError

    def eval_list(self, nodes: list[ast.AST]) -> list[nodes.SourceElement]:
        return [self.eval_single_node(node) for node in nodes]
