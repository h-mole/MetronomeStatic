from PyBirdViewCode.clang_utils.code_attributes.utils import parse_file
from PyBirdViewCode.universal_ast.c_cpp_converter import ClangASTConverter
from PyBirdViewCode.universal_ast import (
    universal_ast_nodes as nodes,
    universal_ast_types as types,
)
from PyBirdViewCode.utils.files import FileManager, abspath_from_file
from tests.base import asset_path
from PyBirdViewCode.clang_utils import beautified_print_ast
from PyBirdViewCode.universal_ast.queries.query_variables import get_all_globals

file_manager = FileManager(abspath_from_file("output", __file__))


def test_c_types_extraction():
    file = asset_path("universal-ast-extraction/global-variables.c")
    converter = ClangASTConverter()
    cursor = parse_file(
        file,
    ).cursor
    assert cursor is not None

    uast = converter.eval(cursor)
    # file_manager.json_dump("c-global-variables_uast.json", uast.to_dict())
    # print(uast)
    get_all_globals(uast)