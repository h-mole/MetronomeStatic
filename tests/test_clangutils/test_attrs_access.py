from dataclasses import dataclass

from PyBirdViewCode import *
from PyBirdViewCode.clang_utils import *
from tests import base


@dataclass
class AttributeAccess:
    variable: str


def traversal_handler(ctx: TraversalContext):
    if ctx.current_node.spelling.startswith("g_"):
        print(ctx.current_node.spelling)
        ctx.print_hierarchy()
        for item in reversed(ctx.hierarchy):
            # print(item.kind, item.spelling)
            # if item.kind == CursorKind.DECL_REF_EXPR:
            #     chain.append()
            if item.kind in (
                CursorKind.DECL_REF_EXPR,
                CursorKind.UNEXPOSED_EXPR,
                CursorKind.ARRAY_SUBSCRIPT_EXPR,
                CursorKind.MEMBER_REF_EXPR,
            ):
                print(item.kind, item.spelling)
            else:
                break


def test_attrs_access():
    cursor = parse_file(base.asset_path("extractor-demos/props_access.c")).cursor
    traversal(cursor).map(traversal_handler).l
