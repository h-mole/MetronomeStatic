import os
import sys

from clang import cindex

from PyBirdViewCode.clang_utils import CompilerArgsType, parse_file

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
ASSETS_PATH = os.path.join(os.path.dirname(__file__), "assets")

pj = os.path.join


def asset_path(p: str) -> str:
    return pj(ASSETS_PATH, p)


def clangutils_load_ast(filename: str, args: CompilerArgsType = None) -> cindex.Cursor:
    c_file = os.path.join(ASSETS_PATH, filename)
    root = parse_file(c_file, args=args).cursor
    return root
