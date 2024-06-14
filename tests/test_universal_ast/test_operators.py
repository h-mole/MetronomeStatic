from PyBirdViewCode import uast
from tests.base import asset_path
from PyBirdViewCode.clang_utils import beautified_print_ast
import networkx as nx
from tests.test_universal_ast.base import extract_uast_from_c


def test_assignment_operators():
    ast = extract_uast_from_c("universal-ast-extraction/test_operators.c")
    f = (
        ast.filter_by(uast.MethodDecl)
        .filter(lambda method: method.name.id == "test_assignments")
        .head()
    )
    symbols = f.filter_by(uast.Assignment).map(lambda expr: expr.operator).l
    assert symbols == (
        [
            "=",
            "+=",
            "-=",
            "*=",
            "/=",
            "%=",
            "<<=",
            ">>=",
            "&=",
            "|=",
            "^=",
        ]
    )


def test_binary_operators():
    ast = extract_uast_from_c("universal-ast-extraction/test_operators.c")
    f = (
        ast.filter_by(uast.MethodDecl)
        .filter(lambda method: method.name.id == "test_binary_operators")
        .head()
    )
    symbols = f.filter_by(uast.BinaryExpr).map(lambda expr: expr.operator).l
    assert symbols == (
        ["+", "-", "*", "/", "%", "&", "|", "^", "<<", ">>"]
        + ["==", "!=", ">=", "<=", "<", ">"]
        + ["||", "&&"]
    )


def test_unary_operators():
    ast = extract_uast_from_c("universal-ast-extraction/test_operators.c")
    f = (
        ast.filter_by(uast.MethodDecl)
        .filter(lambda method: method.name.id == "test_unary_operators")
        .head()
    )
    symbols = (
        f.filter_by(uast.UnaryExpr).map(lambda expr: (expr.sign, expr.op_before_expr)).l
    )
    assert symbols == [
        ("+", True),
        ("-", True),
        ("!", True),
        ("*", True),
        ("&", True),
        ("++", False),
        ("++", True),
        ("--", False),
        ("--", True),
    ]
