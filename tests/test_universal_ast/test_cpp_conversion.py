from MetronomeStatic.clang_utils.code_attributes.utils import get_func_decl, parse_file
from MetronomeStatic.universal_ast.c_cpp_converter import ClangASTConverter
from tests.base import asset_path


def test_cpp_conversion():
    file = asset_path("evaluator-demos/demo1.c")
    decl = get_func_decl(
        parse_file(
            file,
        ).cursor,
        "use_config",
    )
    assert decl is not None
    evaluator = ClangASTConverter()
    evaluator.eval(decl)
