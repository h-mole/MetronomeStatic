from typing import Any, Callable, Dict, Union
import parso
from parso.tree import NodeOrLeaf
from parso.python.tree import PythonNode, Operator
import parso.python.tree as parso_tree
from ..uast import universal_ast_nodes as nodes


class ParsoASTConverter:
    def __init__(
        self,
    ) -> None:
        # self.source_location_filter: Optional[Callable[[SourceLocation], bool]] = None
        self._handlers_map: Dict[str, Callable[[NodeOrLeaf], Any]] = {
            "arith_expr": self._handle_arith_expr,
            "name": self._handle_name,
            "number": self._handle_number,
            "expr_stmt": self._handle_expr_stmt,
            "yield_expr": self._handle_yield_expr,
            "if_stmt": self._handle_if_stmt,
            "funcdef": self._handle_funcdef,
            "suite": self._handle_suite,
            # "newline": lambda _: (),
            "simple_stmt": lambda stmt: self.eval_single_node(stmt.children[0]),
            "while_stmt": self._handle_while,
            "atom": self._handle_atom,
            "return_stmt": self._handle_return,
            "keyword": self._handle_keyword,
        }

        # Return value of execution
        self._ret_value = None
        # self._labels: Dict[str, LabelDesc] = {}

    def _handle_keyword(self, c: parso_tree.ReturnStmt) -> nodes.ReturnStmt:
        if c.value == "return":
            return nodes.ReturnStmt()
        else:
            raise NotImplementedError(c)

    def _handle_return(self, c: parso_tree.Keyword) -> nodes.Stmt:
        print(c.children)
        returned_value = c.children[1]
        match returned_value:
            case PythonNode(type="testlist_star_expr"):

                return nodes.ReturnStmt(
                    [
                        self.eval_single_node(val)
                        for val in returned_value.children
                        if val.type not in ("operator",)
                    ]
                )
            case _:
                return nodes.ReturnStmt([self.eval_single_node(returned_value)])

    def _handle_atom(self, c: parso_tree.PythonNode) -> nodes.Expr:
        if len(c.children) == 3:
            match (c.children[0], c.children[2]):
                case (parso_tree.Operator(value="("), parso_tree.Operator(value=")")):
                    return self.eval_single_node(c.children[1])
        raise NotImplementedError

    def _handle_while(self, c: parso_tree.WhileStmt) -> nodes.WhileStmt:
        print(c, c.children)
        operator_node = c.children[1]
        body_node = c.children[3]
        # raise NotImplementedError
        return nodes.WhileStmt(
            self.eval_single_node(operator_node), self.eval_single_node(body_node)
        )

    def _handle_suite(self, c: parso_tree.PythonNode) -> nodes.BlockStmt:

        return nodes.BlockStmt(
            [
                self.eval_single_node(stmt)
                for stmt in c.children
                if stmt.type not in ("newline")
            ]
        )

    def _handle_funcdef(self, c: parso_tree.Function) -> nodes.MethodDecl:
        # param: parso_tree.Param
        # param.
        method_type = nodes.MethodType(
            [
                nodes.ParamDecl(self.eval_single_node(param.name), nodes.UnknownType("any"))
                for param in c.get_params()
            ],
            nodes.UnknownType("any"),
        )
        method_decl = nodes.MethodDecl(
            self.eval_single_node(c.name),
            method_type,
            self.eval_single_node(c.children[-1]),
            # c.iter
        )
        return method_decl

    def _handle_notimplemented(self, c: NodeOrLeaf) -> nodes.NotImplementedItem:
        return nodes.NotImplementedItem(str(c.kind))

    def _handle_name(self, node: parso_tree.Name) -> nodes.Name:
        return nodes.Name(node.value)

    def _handle_yield_expr(self, node: parso_tree.YieldExpr) -> nodes.Yield:
        _, value = node.children
        return nodes.Yield(self.eval_single_node(value))

    def _handle_if_stmt(self, node: parso_tree.IfStmt) -> nodes.IfThenElseStmt:
        # print(node.children)
        _, namedexpr_test, _, suite, *remainings = node.children
        stmt = nodes.IfThenElseStmt(
            self.eval_single_node(namedexpr_test), self.eval_single_node(suite)
        )
        assert len(remainings) == 0
        return stmt

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

    def _handle_number(self, node: parso_tree.Number) -> nodes.Literal:
        return nodes.Literal(node.value, "number")

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

    def eval_single_node(self, node: NodeOrLeaf) -> nodes.SourceElement:
        try:
            return self._handlers_map[node.type](node)
        except KeyError as e:
            print(node, node.type)
            print(e)
            raise ValueError
