import json
import os
from pprint import pprint
from PyBirdViewCode.clang_utils.code_attributes.utils import get_func_decl, parse_file
from PyBirdViewCode.uast.c_cpp_converter import ClangASTConverter
from PyBirdViewCode.uast.universal_cfg_extractor import CFGBuilder
from PyBirdViewCode.uast import (
    universal_ast_nodes as nodes,
    universal_ast_types as types,
)
from PyBirdViewCode.utils.files import FileManager, abspath_from_file
from tests.base import asset_path
from PyBirdViewCode.clang_utils import beautified_print_ast
import networkx as nx

file_manager = FileManager(abspath_from_file("output", __file__))


def test_cfg_extraction_1():
    file = asset_path("universal-ast-extraction/demo1.c")
    evaluator = ClangASTConverter()
    cursor = get_func_decl(
        parse_file(
            file,
        ).cursor,
        "basic_control_structures",
    )
    assert cursor is not None

    beautified_print_ast(cursor, "out1.json")
    ret = evaluator.eval(cursor)
    print(ret)
    cb = CFGBuilder()
    cfg = cb.build(ret)

    print(cfg.print_graph())

    graph = cfg.to_networkx()
    nx.nx_pydot.write_dot(graph, "out1.dot")


def test_cfg_extraction_2():
    file = asset_path("universal-ast-extraction/demo2.c")
    evaluator = ClangASTConverter()
    cursor = get_func_decl(
        parse_file(
            file,
        ).cursor,
        "basic_control_structures",
    )
    assert cursor is not None

    beautified_print_ast(cursor, "out.json")
    ret = evaluator.eval(cursor)
    print(ret)
    cb = CFGBuilder()
    cfg = cb.build(ret)

    graph = cfg.to_networkx()
    nx.nx_pydot.write_dot(graph, "out.dot")


def test_cfg_extraction_3():
    file = asset_path("universal-ast-extraction/demo3.c")
    evaluator = ClangASTConverter()
    cursor = get_func_decl(
        parse_file(
            file,
        ).cursor,
        "basic_control_structures",
    )
    assert cursor is not None

    beautified_print_ast(cursor, "out.json")
    ret = evaluator.eval(cursor)

    # json_file = "cfg_extraction_3.json"
    # file_manager.json_dump(json_file, ret.to_dict())
    # ast = SourceElement.from_dict(file_manager.json_load(json_file))

    cb = CFGBuilder()
    cfg = cb.build(ret)

    graph = cfg.to_networkx()
    nx.nx_pydot.write_dot(graph, "out.dot")


def test_cfg_extraction_error_handling():
    file = asset_path("universal-ast-extraction/error-handling.c")
    evaluator = ClangASTConverter()
    cursor = get_func_decl(
        parse_file(
            file,
        ).cursor,
        "handle_error_demo",
    )
    assert cursor is not None

    beautified_print_ast(cursor, "out.json")
    ret = evaluator.eval(cursor)
    print(ret)
    cb = CFGBuilder()
    cfg = cb.build(ret)

    print(cfg.print_graph())
    file_manager.json_dump("handle-error-demo.json", ret.to_dict())

    graph = cfg.to_networkx()
    file_manager.dot_dump(
        "handling-errors.dot",
        graph,
    )
