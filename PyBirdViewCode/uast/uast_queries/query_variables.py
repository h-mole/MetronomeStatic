from typing import List, Union
from MelodieFuncFlow import MelodieGenerator
from ...uast import universal_ast_nodes as nodes


def get_all_globals(ast: nodes.CompilationUnit) -> List[nodes.VarDecl]:
    """
    Get all globals from one file
    """
    all_globals = []

    def search_global_def_in_uast(ctx: nodes.SourceElement.ApplyContext) -> bool:
        """
        Search global definitions in the UAST
        """
        if ctx.current_node.__class__ in {nodes.MethodDecl}:
            return False
        if isinstance(ctx.current_node, (nodes.VarDecl,)):
            all_globals.append(ctx.current_node)
        return True

    ast.apply_with_hierarchy(search_global_def_in_uast)
    return all_globals


def get_all_locals(
    ast: Union[nodes.MethodDecl, nodes.NameSpaceDef]
) -> List[nodes.VarDecl]:
    """
    Get all local variable declarations from ast
    """
    return ast.filter_by(nodes.VarDecl).l
