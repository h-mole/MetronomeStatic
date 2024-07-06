from typing import Any, Callable, Dict

import ast
from PyBirdViewCode.uast import ParsoASTConverter, universal_ast_nodes as nodes


def parse_py_code(code: str, version="3.9"):
    module = ast.parse(code)
    expr = module.body[0]
    ret = ParsoASTConverter(set()).eval(expr)
    return ret


def test_assignment():
    ret = parse_py_code("a: int = hello + 1")
    assert ret.filter_by(nodes.BinaryExpr).head().operator == "+"
    assert ret.filter_by(nodes.Assignment).head().operator == "="
    assert ret.filter_by(nodes.Assignment).head().lhs[0].id == "a"

    ret = parse_py_code("a = hello + 1")
    assert ret.filter_by(nodes.BinaryExpr).head().operator == "+"
    assert ret.filter_by(nodes.Assignment).head().operator == "="
    assert ret.filter_by(nodes.Assignment).head().lhs[0].id == "a"

    ret = parse_py_code("a = b = 1")
    assert ret.filter_by(nodes.Assignment).l.__len__() == 2

    ret = parse_py_code("a = b = 1")
    assert ret.filter_by(nodes.Assignment).l.__len__() == 2

    ret = parse_py_code("a += 1")
    assert ret.filter_by(nodes.Assignment).head().operator == "+="

    ret = parse_py_code("a += yield b")
    assignment = ret.filter_by(nodes.Assignment).head()
    assert assignment.operator == "+="
    assert isinstance(assignment.rhs[0], nodes.Yield)
    assert assignment.rhs[0].value.id == "b"
