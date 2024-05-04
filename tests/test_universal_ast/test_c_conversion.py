import json
import os
from pprint import pprint
from PyBirdViewCode.clang_utils.code_attributes.utils import get_func_decl, parse_file
from PyBirdViewCode.universal_ast.c_cpp_converter import ClangASTConverter
from PyBirdViewCode.universal_ast.universal_ast_nodes import SourceElement
from PyBirdViewCode.universal_ast.universal_cfg_extractor import CFGBuilder
from PyBirdViewCode.universal_ast import (
    universal_ast_nodes as nodes,
    universal_ast_types as types,
)
from PyBirdViewCode.utils.files import FileManager, abspath_from_file
from tests.base import asset_path
from PyBirdViewCode.clang_utils import beautified_print_ast
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


def test_c_types_extraction():
    file = asset_path("universal-ast-extraction/c-types.c")
    evaluator = ClangASTConverter()
    cursor = parse_file(
        file,
    ).cursor
    assert cursor is not None

    ret = evaluator.eval(cursor)
    print(ret)

    beautified_print_ast(
        cursor, file_manager.get_abspath("c_types_extracted_clang.json")
    )
    print(ret)
    file_manager.json_dump("c_types_uast.json", ret.to_dict())


def test_conv_real_code():
    file = asset_path("universal-ast-extraction/lua-preprocessed.i")
    evaluator = ClangASTConverter()
    cursor = parse_file(
        file,
    ).cursor
    assert cursor is not None

    ret = evaluator.eval(cursor)
    file_manager.json_dump("real_code_lua_uast.json", ret.to_dict())


def test_variable_types():
    file = asset_path("universal-ast-extraction/variable-types.c")
    evaluator = ClangASTConverter()
    cursor = parse_file(
        file,
    ).cursor
    assert cursor is not None
    beautified_print_ast(cursor, file_manager.get_abspath("variable-types-clang.json"))

    ret = evaluator.eval(cursor)
    file_manager.json_dump("variable-types-uast.json", ret.to_dict())
    node = ret.iter_nodes().filter(lambda c: isinstance(c, nodes.CallExpr)).head()
    assert node.name.id == "register_func"

    ret2 = ret.filter_by(nodes.VarDecl).filter(lambda c: c.variable == "g_func").head()
    assert isinstance(ret2.type, types.CallableType)

    main_ast = ret.filter_by(nodes.MethodDecl).filter(lambda n: n.name == "main").head()
    compound_decls = main_ast.filter_by(nodes.CompoundDecl).l
    assert len(compound_decls) == 4

    assert main_ast.filter_by(nodes.VarDecl).map(lambda n: n.variable.id).s == {
        "a",
        "b",
        "c",
        "d",
        "e",
        "a1",
    }
    # 扫描a1.func的调用
    a1_func_prop_call = (
        main_ast.filter_by(nodes.CallExpr)
        .filter(
            lambda node: isinstance(node.name, nodes.FieldAccessExpr)
            and node.name.name == "func"
        )
        .head()
    )
    assert len(a1_func_prop_call.arguments) == 2
    # 扫描对a1.func的赋值
    assignment = main_ast.filter_by(nodes.Assignment).head()
    assert isinstance(assignment.lhs, nodes.FieldAccessExpr)
    assert isinstance(assignment.rhs, nodes.Name) and assignment.rhs.id == "add"

    struct_def_ast = ret.filter_by(nodes.Type, name="A").head()
    assert isinstance(struct_def_ast.type_arguments, nodes.StructDecl)
    assert struct_def_ast.filter_by(nodes.FieldDecl).map(lambda node: node.name).s == {
        "a",
        "func",
    }
