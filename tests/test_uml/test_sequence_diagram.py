import json
import os
from PyBirdViewCode.clang_utils.code_attributes.utils import get_func_decl, parse_file
from PyBirdViewCode.universal_ast.c_cpp_converter import ClangASTConverter
from PyBirdViewCode.universal_ast.universal_ast_nodes import SourceElement
from PyBirdViewCode.universal_ast.universal_cfg_extractor import CFGBuilder
from PyBirdViewCode.utils.files import FileManager, abspath_from_file
from tests.base import asset_path
from PyBirdViewCode.clang_utils import beautified_print_ast
from PyBirdViewCode.uml_utils.SequenceDiagram import ast_to_diagram
import networkx as nx

file_manager = FileManager(abspath_from_file("output", __file__))


def test_cfg_extraction_error_handling():
    file = asset_path("uml/sequence-diagram.c")
    evaluator = ClangASTConverter()
    cursor = get_func_decl(
        parse_file(
            file,
        ).cursor,
        "func1",
    )
    assert cursor is not None

    beautified_print_ast(cursor, "out.json")
    ret = evaluator.eval(cursor)
    # print(ret)
    # cb = CFGBuilder()
    # cb.build(ret)

    # print(cb.print_graph())
    file_manager.json_dump("handle-error-demo.json", ret.to_dict())

    # graph = cb.to_networkx()
    # file_manager.dot_dump(
    #     "handling-errors.dot",
    #     graph,
    # )

    ast_to_diagram(ret, file_manager.get_abspath("handling-errors.plantuml"))