from textwrap import indent
from typing import Callable, Dict, Type

from ...uast import universal_ast_nodes as nodes


class BaseUASTUnparser:
    """
    The base class of UAST unparser for generating code.
    """

    def __init__(self) -> None:
        self.handler: Dict[
            Type[nodes.SourceElement], Callable[[nodes.SourceElement], str]
        ] = {
            nodes.BinaryExpr: self.unparse_binary_expr,
            nodes.Name: self.unparse_name,
            nodes.Literal: self.unparse_literal,
            nodes.Assignment: self.unparse_assignment,
            nodes.VarDecl: self.unparse_var_decl,
            nodes.CompoundDecl: self.unparse_compound_decl,
            nodes.IntType: self.unparse_int_type,
            nodes.FloatType: self.unparse_float_type,
            nodes.UnknownType: lambda t: t.type,
            nodes.UserDefinedType: self.unparse_user_defined_type,
            nodes.ArrayInitializer: self.unparse_array_initializer,
            nodes.FieldAccessExpr: self.unparse_field_access_expr,
            nodes.ArrayAccessExpr: self.unparse_array_access_expr,
            nodes.UnaryExpr: self.unparse_unary_expr,
            nodes.VoidType: lambda t: "void",
            # nodes.ArrayType: self.unparse_arr
        }

    def unparse_array_access_expr(self, expr: nodes.ArrayAccessExpr):
        return f"{self.unparse(expr.target)}[{self.unparse(expr.index)}]"

    def unparse_field_access_expr(self, expr: nodes.FieldAccessExpr):
        return f"{self.unparse(expr.target)}.{expr.name}"

    def unparse_user_defined_type(self, typedef: nodes.UserDefinedType):
        return typedef.name

    def unparse_array_initializer(self, expr: nodes.ArrayInitializer):
        return f"{{{', '.join([self.unparse(item) for item in expr.elements])}}}"

    def unparse_float_type(self, expr: nodes.FloatType):
        mapping = {32: "float", 64: "double"}
        return mapping.get(expr.bits, "double")

    def unparse_int_type(self, expr: nodes.IntType):
        mapping = {8: "char", 16: "short", 32: "int", 64: "long long"}
        int_type_str = mapping.get(expr.bits, "int")
        if expr.signed:
            return int_type_str
        else:
            return f"unsigned {int_type_str}"

    def unparse_assignment(self, expr: nodes.Assignment):
        assert len(expr.lhs) == 1
        return (
            f"{self.unparse(expr.lhs[0])} {expr.operator} {self.unparse(expr.rhs[0])}"
        )

    def unparse_binary_expr(self, expr: nodes.BinaryExpr):
        return f"{self.unparse(expr.lhs)} {expr.operator} {self.unparse(expr.rhs)}"

    def unparse_unary_expr(self, expr: nodes.UnaryExpr):
        if expr.op_before_expr:
            return f"{expr.sign} {self.unparse(expr.expression)}"
        else:
            return f"{self.unparse(expr.expression)} {expr.sign}"

    def unparse_compound_decl(self, expr: nodes.CompoundDecl):
        return ";".join([self.unparse(item) for item in expr.decls])

    def unparse_var_decl(self, expr: nodes.VarDecl):
        if isinstance(expr.type, nodes.ArrayType):
            head = f"{self.unparse(expr.type.elem_type)} {self.unparse(expr.variable)}[{expr.type.length}]"
        else:
            head = f"{self.unparse(expr.type)} {self.unparse(expr.variable)}"
        if expr.initializer:
            return head + " = " + self.unparse(expr.initializer) + ";"
        else:
            return head + ";"

    def unparse_literal(self, expr: nodes.Literal):
        return str(expr.value)

    def unparse_name(self, expr: nodes.Name):
        return expr.id

    def unparse(self, stmt: nodes.SourceElement):
        try:
            return self.handler[stmt.__class__](stmt)
        except KeyError as e:
            print(stmt)
            raise e

    def unparse_indented(self, stmt: nodes.SourceElement):
        return indent(self.unparse(stmt), "    ")
