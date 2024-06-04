from MelodieFuncFlow import MelodieGenerator
from ...universal_ast import universal_ast_nodes as nodes


def search_global_def_in_uast(ctx: nodes.SourceElement.ApplyContext) -> bool:
    """
    Search global definitions in the UAST
    """
    # print(ctx)
    if ctx.current_node.__class__ in {nodes.MethodDecl}:
        return False
    # print(ctx)
    if isinstance(ctx.current_node, (nodes.VarDecl,)):
        print(ctx.current_node)
    return True


def get_all_globals(ast: nodes.CompilationUnit):
    # print(ast)
    ast.apply_with_hierarchy(search_global_def_in_uast)
