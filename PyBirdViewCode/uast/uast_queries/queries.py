from typing import Callable, List, Union
from MelodieFuncFlow import MelodieGenerator
from .. import universal_ast_nodes as nodes


# class FiltersCreator:
def create_method_name_filter(
    method_name: str,
) -> Callable[[nodes.SourceElement], bool]:
    def wrapper(method: nodes.SourceElement):
        match method:
            case nodes.MethodDecl(name=nodes.Name(id=name_id)):
                return name_id == method_name
            case _:
                return False

    return wrapper


class UASTQuery:
    @classmethod
    def get_all_globals(cls, uast: nodes.SourceElement) -> List[nodes.VarDecl]:
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

        uast.apply_with_hierarchy(search_global_def_in_uast)
        return all_globals

    @classmethod
    def get_all_params(cls, uast: nodes.MethodDecl) -> list[nodes.ParamDecl]:
        """
        Get all parameter from the method or function
        """
        return uast.filter_by(nodes.ParamDecl).l

    @classmethod
    def get_all_locals(
        cls, uast: Union[nodes.MethodDecl, nodes.NameSpaceDef]
    ) -> List[nodes.VarDecl]:
        """
        Get all local variable declarations from uast
        uast should be:
        """
        return uast.filter_by(nodes.VarDecl).l

    @classmethod
    def get_method_by_name(
        cls, uast: nodes.SourceElement, name: str
    ) -> nodes.MethodDecl:
        """
        Get method declaration by name
        :param name: name of method
        :return: MethodDecl
        """
        try:
            return (
                uast.filter_by(nodes.MethodDecl)
                .filter(create_method_name_filter(name))
                .head()
            )
        except StopIteration:
            raise ValueError(f"No method named `{name}` found in this uast")
