from typing import Iterable, List, Optional

import tests.base as base
from MetronomeStatic.clang_utils import (
    Cursor,
    CursorKind,
    get_func_decl,
    iter_ast,
    split_for_loop_conditions,
)


def check_result(
    results: Iterable[Optional[Cursor]], expected_results: List[Optional[CursorKind]]
):
    for result, expected_result in zip(results, expected_results):
        if expected_result is not None:
            assert (result is not None) and expected_result == result.kind
        else:
            assert result is None


def load_for_stmt(func_name: str) -> Cursor:
    c = base.clangutils_load_ast("extractor-demos/control-structures.c")
    func_decl = get_func_decl(c, func_name)
    assert func_decl is not None
    return iter_ast(func_decl).filter(lambda c: c.kind == CursorKind.FOR_STMT).head()


def test_split_loop_conds_omitting_stmt_before():
    for_stmt_ast = load_for_stmt("for_demo_omitting_1")
    res = split_for_loop_conditions(for_stmt_ast)
    check_result(
        res,
        [
            None,
            CursorKind.BINARY_OPERATOR,
            CursorKind.UNARY_OPERATOR,
            CursorKind.COMPOUND_STMT,
        ],
    )


def test_split_loop_conds_omitting_2():
    for_stmt_ast = load_for_stmt("for_demo_omitting_2")
    res = split_for_loop_conditions(for_stmt_ast)
    check_result(
        res,
        [
            CursorKind.DECL_STMT,
            None,
            CursorKind.UNARY_OPERATOR,
            CursorKind.COMPOUND_STMT,
        ],
    )


def test_split_loop_conds_omitting_3():
    for_stmt_ast = load_for_stmt("for_demo_omitting_3")
    res = split_for_loop_conditions(for_stmt_ast)
    check_result(
        res,
        [
            CursorKind.DECL_STMT,
            CursorKind.BINARY_OPERATOR,
            None,
            CursorKind.COMPOUND_STMT,
        ],
    )


def test_split_loop_conds_omitting_1_3():
    for_stmt_ast = load_for_stmt("for_demo_omitting_1_3")
    res = split_for_loop_conditions(for_stmt_ast)
    check_result(
        res,
        [
            None,
            CursorKind.BINARY_OPERATOR,
            None,
            CursorKind.COMPOUND_STMT,
        ],
    )


def test_split_loop_conds_omitting_1_2():
    for_stmt_ast = load_for_stmt("for_demo_omitting_1_2")
    res = split_for_loop_conditions(for_stmt_ast)
    check_result(
        res,
        [
            None,
            None,
            CursorKind.UNARY_OPERATOR,
            CursorKind.COMPOUND_STMT,
        ],
    )


def test_split_loop_conds_omitting_2_3():
    for_stmt_ast = load_for_stmt("for_demo_omitting_2_3")
    res = split_for_loop_conditions(for_stmt_ast)
    check_result(
        res,
        [
            CursorKind.DECL_STMT,
            None,
            None,
            CursorKind.COMPOUND_STMT,
        ],
    )


def test_split_loop_conds_omitting_all():
    for_stmt_ast = load_for_stmt("for_demo_omitting_all")
    res = split_for_loop_conditions(for_stmt_ast)
    check_result(
        res,
        [
            None,
            None,
            None,
            CursorKind.COMPOUND_STMT,
        ],
    )


def test_split_loop_conds_omitting_all():
    for_stmt_ast = load_for_stmt("for_demo_omitting_body")
    res = split_for_loop_conditions(for_stmt_ast)
    check_result(
        res,
        [
            CursorKind.DECL_STMT,
            CursorKind.BINARY_OPERATOR,
            CursorKind.UNARY_OPERATOR,
            CursorKind.COMPOUND_ASSIGNMENT_OPERATOR,
        ],
    )


def test_split_loop_conds_1():
    for_stmt_ast = load_for_stmt("for_demo_1")
    res = split_for_loop_conditions(for_stmt_ast)
    check_result(
        res,
        [
            CursorKind.DECL_STMT,
            CursorKind.BINARY_OPERATOR,
            CursorKind.UNARY_OPERATOR,
            CursorKind.COMPOUND_STMT,
        ],
    )
