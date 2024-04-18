import json
import os
from MetronomeStatic.clang_utils.code_attributes.utils import get_func_decl, parse_file
from MetronomeStatic.universal_ast.c_cpp_converter import ClangASTConverter
from MetronomeStatic.universal_ast.universal_ast_nodes import SourceElement
from MetronomeStatic.universal_ast.universal_cfg_extractor import CFGBuilder
from MetronomeStatic.utils.files import FileManager, abspath_from_file
from tests.base import asset_path
from MetronomeStatic.clang_utils import beautified_print_ast
import networkx as nx

file_manager = FileManager(abspath_from_file("output", __file__))


def test_cpp_conversion():
    file = asset_path("evaluator-demos/demo1.c")
    evaluator = ClangASTConverter()
    cursor = parse_file(
        file,
    ).cursor

    beautified_print_ast(cursor, "out.json")
    ret = evaluator.eval(cursor)
    print(ret)


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
    cb.build(ret)

    print(cb.print_graph())

    graph = cb.to_networkx()
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
    cb.build(ret)

    print(cb.print_graph())

    graph = cb.to_networkx()
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
    cb.build(ret)

    print(cb.print_graph())

    graph = cb.to_networkx()
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
    cb.build(ret)

    print(cb.print_graph())
    file_manager.json_dump("handle-error-demo.json", ret.to_dict())

    graph = cb.to_networkx()
    file_manager.dot_dump(
        "handling-errors.dot",
        graph,
    )
