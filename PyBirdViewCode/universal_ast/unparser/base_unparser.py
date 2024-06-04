from ...universal_ast import universal_ast_nodes as nodes


class BaseUASTUnparser:
    """
    The base class of UAST unparser for generating code.
    """
    def __init__(self) -> None:
        self.handler = {
            nodes.BinaryExpr: self.unparse_binary_expr,
            nodes.Name: self.unparse_name,
            nodes.Literal: self.unparse_literal,
            nodes.Assignment: self.unparse_assignment,
        }

    def unparse_assignment(self, expr: nodes.Assignment):
        assert len(expr.lhs) == 1
        return (
            f"{self.unparse(expr.lhs[0])} {expr.operator} {self.unparse(expr.rhs[0])}"
        )

    def unparse_binary_expr(self, expr: nodes.BinaryExpr):
        return f"{self.unparse(expr.lhs)} {expr.operator} {self.unparse(expr.rhs)}"

    def unparse_unary_expr(self, expr: nodes.UnaryExpr):
        if expr.op_before_expr:
            return f"{self.operator} {self.unparse(expr.expression)}"
        else:
            return f"{self.unparse(expr.expression)} {self.operator}"

    def unparse_literal(self, expr: nodes.Literal):
        return str(expr.value)

    def unparse_name(self, expr: nodes.Name):
        return expr.id

    def unparse(self, stmt: nodes.SourceElement):
        return self.handler[stmt.__class__](stmt)
