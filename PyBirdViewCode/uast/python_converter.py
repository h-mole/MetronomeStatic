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
        }

        # Return value of execution
        self._ret_value = None
        # self._labels: Dict[str, LabelDesc] = {}

    def _handle_notimplemented(self, c: NodeOrLeaf) -> nodes.NotImplementedItem:
        return nodes.NotImplementedItem(str(c.kind))

    def _handle_name(self, node: parso_tree.Name) -> nodes.Name:
        return nodes.Name(node.value)

    def _handle_yield_expr(self, node: parso_tree.YieldExpr) -> nodes.Yield:
        _, value = node.children
        return nodes.Yield(self.eval_single_node(value))

    def _handle_if_stmt(self, node: parso_tree.IfStmt) -> nodes.IfThenElseStmt:
        # print(node.children)
        _, namedexpr_test, _, suite, *remainings = nodes.children
        raise NotImplementedError

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
            print(node)
            raise e
