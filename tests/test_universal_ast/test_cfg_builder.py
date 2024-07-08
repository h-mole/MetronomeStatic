from PyBirdViewCode.clang_utils.code_attributes.utils import get_func_decl, parse_file
from PyBirdViewCode.uast import (
    ClangASTConverter,
    extract_cfg_from_method,
    UASTQuery,
    get_file_uast,
)
from PyBirdViewCode.uast.universal_cfg_extractor import (
    CFGBuilder,
)
from PyBirdViewCode.utils.files import FileManager, abspath_from_file
from tests.base import asset_path
from PyBirdViewCode.clang_utils import beautified_print_ast
import networkx as nx
from tests.test_universal_ast.base import verify_topology

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

    cb = CFGBuilder()
    cfg = cb.build(ret)

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

    cb = CFGBuilder()
    cfg = cb.build(ret, True, True)

    graph = cfg.to_networkx()
    file_manager.dot_dump(
        graph,
        "test_cfg_extraction_2.dot",
    )


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

    cb = CFGBuilder()
    cfg = cb.build(ret)

    graph = cfg.to_networkx()
    nx.nx_pydot.write_dot(graph, "out.dot")


def test_cfg_extraction_error_handling():
    file = asset_path("universal-ast-extraction/error-handling.c")

    uast = UASTQuery.get_method(get_file_uast(file), "handle_error_demo")
    cfg = extract_cfg_from_method(uast)

    graph = cfg.to_networkx()
    file_manager.dot_dump(
        graph,
        "handling-errors.dot",
    )
    verify_topology(
        [(1, 4), (4, 8), (4, 3), (3, 2), (8, 7), (8, 3), (6, 3), (7, 8), (7, 6)], graph
    )


def test_expand_multi_stmt():
    file = asset_path("universal-ast-extraction/control-flow-multi-stmt.c")
    uast = UASTQuery.get_method(get_file_uast(file), "main")
    cfg = extract_cfg_from_method(uast)
    expected_topology = [(4, 6), (4, 2), (6, 2), (7, 8), (8, 9), (9, 10), (10, 4)]
    file_manager.dot_dump(cfg.to_networkx(), "cfg-not-expanded-main.dot")
    verify_topology(expected_topology, cfg.topology)

    uast = UASTQuery.get_method(get_file_uast(file), "main2")
    cfg = extract_cfg_from_method(uast)
    file_manager.dot_dump(cfg.to_networkx(), "cfg-not-expanded.dot")
    verify_topology(
        [
            (1, 4),
            (4, 11),
            (4, 15),
            (11, 12),
            (15, 16),
            (7, 8),
            (8, 9),
            (9, 10),
            (10, 2),
            (12, 13),
            (13, 14),
            (14, 7),
            (16, 7),
        ],
        cfg.topology,
    )
