from typing import Callable, List, Optional, Union
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
    def get_method(
        cls, uast: nodes.SourceElement, method_name: Optional[str] = None
    ) -> nodes.MethodDecl:
        """
        通过指定的条件，获取函数或方法的声明节点，并返回第一个

        :method_name: 函数或方法的名称
        :return: MethodDecl
        """
        try:
            return cls.iter_methods(uast, method_name).head()
        except StopIteration:
            raise ValueError(f"No method named `{method_name}` found in this uast")

    @classmethod
    def iter_methods(
        cls, uast: nodes.SourceElement, method_name: Optional[str] = None
    ) -> MelodieGenerator[nodes.MethodDecl]:
        """
        通过指定的条件，获取函数或方法的声明节点们，并返回一个生成器

        :method_name: 函数或方法的名称
        :return: MethodDecl
        """

        methods_generator = uast.filter_by(nodes.MethodDecl)
        if method_name is not None:
            methods_generator = methods_generator.filter(
                create_method_name_filter(method_name)
            )
        return methods_generator
