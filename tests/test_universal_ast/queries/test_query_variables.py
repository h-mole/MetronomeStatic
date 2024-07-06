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
from PyBirdViewCode.uast.uast_queries import UASTQuery
from MelodieFuncFlow import MelodieGenerator

file_manager = FileManager(abspath_from_file("output", __file__))


def test_c_types_extraction():
    file = asset_path("universal-ast-extraction/global-variables.c")
    converter = ClangASTConverter()
    cursor = parse_file(
        file,
    ).cursor
    assert cursor is not None

    uast = converter.eval(cursor)

    global_vars = UASTQuery.get_all_globals(uast)
    print(global_vars)
    float_arr_decl = (
        MelodieGenerator(global_vars).filter(lambda decl: decl.location[0] == 11).head()
    )
    assert isinstance(float_arr_decl.type, nodes.ArrayType)
    assert isinstance(float_arr_decl.type.elem_type, nodes.FloatType), float_arr_decl
    assert float_arr_decl.type.elem_type.bits == 64
    assert float_arr_decl.type.length == 2


def test_extract_local():
    file = asset_path("universal-ast-extraction/local-variables.c")
    converter = ClangASTConverter()
    cursor = parse_file(
        file,
    ).cursor
    assert cursor is not None

    uast = converter.eval(cursor)
    all_locals = (
        MelodieGenerator(
            UASTQuery.get_all_locals(uast.filter_by(nodes.MethodDecl).head())
        )
        .map(lambda decl: BaseUASTUnparser().unparse(decl.variable))
        .s
    )
    assert all_locals == {"a", "b"}
