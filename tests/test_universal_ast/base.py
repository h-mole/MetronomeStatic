from PyBirdViewCode.clang_utils.code_attributes.utils import parse_file
from PyBirdViewCode.uast.c_cpp_converter import ClangASTConverter
from tests.base import asset_path


def extract_uast_from_c(file: str):
    file = asset_path(file)
    evaluator = ClangASTConverter()
    cursor = parse_file(
        file,
    ).cursor
    assert cursor is not None

    ret = evaluator.eval(cursor)
    return ret
