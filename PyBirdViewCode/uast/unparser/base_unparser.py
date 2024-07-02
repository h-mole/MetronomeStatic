from textwrap import indent, dedent
from typing import Callable, Dict, Type
import warnings

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
            nodes.ReturnStmt: lambda item: f"return {','.join( [self.unparse(res) for res in item.result])}",
            nodes.Label: lambda item: f"{item.name} {self.unparse(item.statement)}&colon",
            nodes.MethodDecl: self.unparse_method_decl,
            nodes.CompilationUnit: self.unparse_compilation_unit,
            nodes.ClassDecl: self.unparse_class_decl,
            nodes.ParamDecl: self.unparse_param_decl,
            nodes.BlockStmt: self.unparse_block_stmt,
            nodes.IfThenElseStmt: self.unparse_if_then_else_stmt,
            nodes.Null: lambda n: "null",
            nodes.ForStmt: self.unparse_for_stmt,
            nodes.WhileStmt: self.unparse_while_stmt,
            nodes.CallExpr: self.unparse_call_expr,
            nodes.BreakStmt: self.unparse_break_stmt,
            nodes.AssertStmt: self.unparse_assert_stmt,
            nodes.ThrowStmt: self.unparse_throw_stmt,
            nodes.NotImplementedItem: lambda x: "notimplemented-" + x.kind,
            nodes.Conditional: lambda expr: f"{self.unparse(expr.predicate)}?{self.unparse(expr.if_true)}:{self.unparse(expr.if_false)}",
            # nodes.ArrayType: self.unparse_arr
        }

    def _eval_statements(self, stmts: list[nodes.Stmt]) -> list[str]:
        def add_semicolon(unparsed, stmt):
            if unparsed == "" or isinstance(stmt, nodes.Stmt):
                return unparsed
            else:
                return unparsed + ";"

        stmts_unparsed = [add_semicolon(self.unparse(stmt), stmt) for stmt in stmts]
        return stmts_unparsed

    def unparse_call_expr(self, expr: nodes.CallExpr):
        """ """
        return f"{self.unparse(expr.name)}({', '.join([self.unparse(arg) for arg in expr.arguments])})"

    def unparse_assert_stmt(self, stmt: nodes.AssertStmt):
        return f"assert({self.unparse(stmt.predicate)})"

    def unparse_throw_stmt(self, stmt: nodes.ThrowStmt):
        return f"throw {self.unparse(stmt.exception)}"

    def unparse_break_stmt(self, stmt: nodes.BreakStmt):
        return "break"

    def unparse_while_stmt(self, stmt: nodes.WhileStmt):
        body_unparsed = self.unparse(stmt.body)

        unparsed = (
            dedent(
                f"""
            while ({self.unparse(stmt.predicate)}) {{
            %s
            }}
            """
            )
            % (indent(body_unparsed, " " * 4))
        )
        return unparsed

    def unparse_for_stmt(self, stmt: nodes.ForStmt):
        if isinstance(stmt.init, nodes.CompoundDecl):
            _1 = self.unparse(stmt.init)
        else:
            raise NotImplementedError(stmt.init)
        # _1 = self.unparse(first_expr)
        # should_break = 0;
        body_unparsed = self.unparse(stmt.body)

        unparsed = (
            dedent(
                f"""
            for ({_1} ;{self.unparse(stmt.predicate) if stmt.predicate is not None else ''} ;{self.unparse(stmt.update)}) {{
            %s
            }}
            """
            )
            % (indent(body_unparsed, " " * 4))
        )
        return unparsed

    def unparse_if_then_else_stmt(self, stmt: nodes.IfThenElseStmt):
        if stmt.if_false is None:
            return (
                dedent(
                    """
                    if (%s) {
                    %s
                    }
                    """
                ).strip()
                % (self.unparse(stmt.predicate), self.unparse_indented(stmt.if_true))
            )
        else:
            # Handle the circumstance like "else-if" structure
            if isinstance(stmt.if_false, nodes.IfThenElseStmt):
                return (
                    (
                        dedent(
                            """
                        if (%s) {
                        %s
                        } else %s
                        """
                        ).lstrip()
                    )
                    % (
                        self.unparse(stmt.predicate),
                        self.unparse_indented(stmt.if_true),
                        self.unparse(stmt.if_false),
                    )
                )
            else:
                return (
                    dedent(
                        """
                    if (%s) {
                    %s
                    } else {
                    %s
                    }
                    """
                    ).lstrip()
                    % (
                        self.unparse(stmt.predicate),
                        self.unparse_indented(stmt.if_true),
                        self.unparse(stmt.if_false),
                    )
                )

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
        return ", ".join([self.unparse(item) for item in expr.decls])

    def unparse_var_decl(self, expr: nodes.VarDecl):
        if isinstance(expr.type, nodes.ArrayType):
            head = f"{self.unparse(expr.type.elem_type)} {self.unparse(expr.variable)}[{expr.type.length}]"
        else:
            head = f"{self.unparse(expr.type) if expr.type is not None else 'Any'} {self.unparse(expr.variable)}"
        if expr.initializer:
            return head + " = " + self.unparse(expr.initializer)
        else:
            return head

    def unparse_literal(self, expr: nodes.Literal):
        return repr(expr.value)

    def unparse_name(self, expr: nodes.Name):
        return expr.id

    def unparse(self, stmt: nodes.SourceElement):
        try:
            return self.handler[stmt.__class__](stmt)
        except KeyError as e:
            warnings.warn(f"cannot unparse {stmt}")
            raise e

    def unparse_indented(self, stmt: nodes.SourceElement):
        return indent(self.unparse(stmt), "    ")

    def unparse_compilation_unit(self, node: nodes.CompilationUnit):
        return "\n\n".join([self.unparse(n) for n in node.children])

    def unparse_block_stmt(self, node: nodes.BlockStmt):
        # if self.loops_level == 0:
        return "\n".join(self._eval_statements(node.statements))
        # else:
        # return self.unparse_block_considering_break(node)

    def unparse_param_decl(self, param_decl: nodes.ParamDecl):
        return f"{self.unparse(param_decl.type) if param_decl.type is not None else 'Any'} {self.unparse(param_decl.name)}"

    def unparse_class_decl(self, decl: nodes.ClassDecl):

        return (
            dedent(
                """
            class %s {
            %s
            }
            """
            )
            % (
                decl.name,
                indent(
                    "\n".join([self.unparse(n) for n in decl.body]),
                    " " * 4,
                ),
                # func_body_str,
            )
        )

    def unparse_method_decl(self, decl: nodes.MethodDecl):
        params = ", ".join([self.unparse(param) for param in decl.type.pos_args])
        func_body_str = self.unparse_indented(decl.body)

        # Allow parsing var decl, to gather all defined local variables
        #  at the beginning of the function
        self.enable_parsing_var_decl = True
        return (
            dedent(
                """
            %s %s (%s) {
            %s
            }
            """
            )
            % (
                self.unparse(decl.type.return_type),
                self.unparse(decl.name),
                params,
                # indent(
                #     "\n".join([self.unparse(var) for var in self.local_variable_defs]),
                #     " " * 4,
                # ),
                func_body_str,
            )
        )
