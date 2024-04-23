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
from PyBirdViewCode.clang_utils import beautified_print_ast
import networkx as nx
from MelodieFuncFlow import MelodieGenerator

file_manager = FileManager(abspath_from_file("output", __file__))


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
    assert isinstance(namespaces[0].children[0], nodes.MethodDeclaration) and namespaces[0].children[0].name == 'func'
    assert isinstance(namespaces[1].children[0], nodes.MethodDeclaration) and namespaces[1].children[0].name == 'func'
