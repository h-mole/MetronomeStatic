import json
import os
from pprint import pprint
from typing import List
from PyBirdViewCode.clang_utils.code_attributes.utils import get_func_decl, parse_file
from PyBirdViewCode.universal_ast.c_cpp_converter import ClangASTConverter
from PyBirdViewCode.universal_ast import universal_ast_nodes as nodes
from PyBirdViewCode.universal_ast.universal_cfg_extractor import CFGBuilder
from PyBirdViewCode.utils.files import FileManager, abspath_from_file
from tests.base import asset_path
from PyBirdViewCode.clang_utils import beautified_print_ast, CursorKind
import networkx as nx
from MelodieFuncFlow import MelodieGenerator

file_manager = FileManager(abspath_from_file("output", __file__))


def cpp_parse_routine(
    file: str,
    clang_json_file_prefix: str,
    uast_file_prefix: str,
    func: str = "",
    cls: str="",
    only_parse_current=False,
):
    evaluator = ClangASTConverter()
    if only_parse_current:
        evaluator.source_location_filter = lambda c: (
            os.path.samefile(file, c.location.file.name) if c.location.file.name else True
        )
    cursor = parse_file(file, ["-xc++", "-std=c++11"]).cursor
    if func != "":
        cursor = get_func_decl(cursor, func)
    elif cls!="":
        cursor = MelodieGenerator(cursor.walk_preorder()).filter(lambda node: node.kind==CursorKind.CLASS_DECL and node.spelling == cls).l[0]
    assert cursor is not None
    beautified_print_ast(
        cursor, file_manager.get_abspath(clang_json_file_prefix + "_clang.json")
    )
    ret = evaluator.eval(cursor)
    file_manager.json_dump(uast_file_prefix + "_uast.json", ret.to_dict())
    return ret


def test_conv_demo1():
    file = asset_path("universal-ast-extraction/cpp_namespaces.cpp")
    evaluator = ClangASTConverter()
    cursor = parse_file(file, ["-xc++", "-std=c++11"]).cursor
    assert cursor is not None
    beautified_print_ast(
        cursor, file_manager.get_abspath("cpp_demo1_extracted_clang.json")
    )
    ret = evaluator.eval(cursor)
    # print(ret)
    file_manager.json_dump("cpp_demo1_uast.json", ret.to_dict())
    namespaces: List[nodes.NameSpaceDef] = (
        MelodieGenerator(ret.walk_preorder())
        .extra_job(print)
        .filter(lambda node: isinstance(node, nodes.NameSpaceDef))
        .cast(nodes.NameSpaceDef)
        .l
    )
    assert len(namespaces) == 2
    assert namespaces[0].name == "first_space"
    assert namespaces[1].name == "second_space"
    assert (
        isinstance(namespaces[0].children[0], nodes.MethodDecl)
        and namespaces[0].children[0].name == "func"
    )
    assert (
        isinstance(namespaces[1].children[0], nodes.MethodDecl)
        and namespaces[1].children[0].name == "func"
    )


def test_conv_cout_endl():
    """
    TODO: cout endl cannot be successfully converted yet.
    """
    file = asset_path("universal-ast-extraction/cpp_output.cpp")
    evaluator = ClangASTConverter()

    cursor = get_func_decl(parse_file(file, ["-xc++", "-std=c++11"]).cursor, "main")
    assert cursor is not None
    beautified_print_ast(cursor, file_manager.get_abspath("cout-endl.json"))
    ret = evaluator.eval(cursor)

    file_manager.json_dump("cout-endl-uast.json", ret.to_dict())


def test_conv_cpp_class():
    file = asset_path("universal-ast-extraction/cpp_class.cpp")
    ast = cpp_parse_routine(file, "cpp_class", "cpp_class", only_parse_current=True)
