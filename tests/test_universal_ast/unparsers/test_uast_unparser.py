from PyBirdViewCode.clang_utils.code_attributes.utils import parse_file
from PyBirdViewCode.uast import ClangASTConverter
from PyBirdViewCode.uast import (
    universal_ast_nodes as nodes,
    universal_ast_types as types,
    BaseUASTUnparser,
)
from PyBirdViewCode.utils.files import FileManager, abspath_from_file
from tests.base import asset_path
from PyBirdViewCode.clang_utils import beautified_print_ast
from PyBirdViewCode.uast import UASTQuery
from MelodieFuncFlow import MelodieGenerator

file_manager = FileManager(abspath_from_file("output", __file__))


def test_data_structure_unparse():
    file = asset_path("universal-ast-extraction/global-variables.c")
    converter = ClangASTConverter()
    cursor = parse_file(
        file,
    ).cursor
    assert cursor is not None

    uast = converter.eval(cursor)

    global_vars = UASTQuery.get_all_globals(uast)
    print(global_vars)
    unparsed = MelodieGenerator(global_vars).map(BaseUASTUnparser().unparse).l
    print(unparsed)
