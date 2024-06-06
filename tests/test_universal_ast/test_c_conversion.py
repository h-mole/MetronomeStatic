from PyBirdViewCode.clang_utils.code_attributes.utils import parse_file
from PyBirdViewCode.uast.c_cpp_converter import ClangASTConverter
from PyBirdViewCode.uast import (
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
    assert isinstance(ret2.type, nodes.MethodType)

    main_ast = ret.filter_by(nodes.MethodDecl).filter(lambda n: n.name.id == "main").head()
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
    assert isinstance(assignment.lhs[0], nodes.FieldAccessExpr)
    assert isinstance(assignment.rhs[0], nodes.Name) and assignment.rhs[0].id == "add"

    struct_def_ast = ret.filter_by(nodes.Type, name="A").head()
    assert isinstance(struct_def_ast.type_arguments, nodes.StructDecl)
    assert struct_def_ast.filter_by(nodes.FieldDecl).map(lambda node: node.name).s == {
        "a",
        "func",
    }
