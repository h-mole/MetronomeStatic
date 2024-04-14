from MetronomeStatic.clang_utils.code_attributes.utils import get_func_decl, parse_file
from MetronomeStatic.universal_ast.c_cpp_converter import ClangASTConverter
from MetronomeStatic.universal_ast.universal_cfg_extractor import CFGBuilder
from tests.base import asset_path
from MetronomeStatic.clang_utils import beautified_print_ast
import networkx as nx


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
    print(ret)
    cb = CFGBuilder()
    cb.build(ret)

    print(cb.print_graph())

    graph = cb.to_networkx()
    nx.nx_pydot.write_dot(graph, "out.dot")