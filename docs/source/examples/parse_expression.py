import sys

sys.path.append("../../..")
from PyBirdViewCode import abspath_from_current_file
from PyBirdViewCode.clang_utils import (
    get_func_decl,
    parse_file,
    get_func_decl,
    CursorKind,
    split_binary_operator,
    split_unary_operator,
    print_tokens,
)


# Load file by clang and get the translation unit
translation_unit = parse_file(
    abspath_from_current_file("assets/parse_expression.c", __file__)
)

# Get the cursor to whole file from Translation Unit
cursor = translation_unit.cursor

# Get the cursor to function demo
func_decl = get_func_decl(cursor, "demo")

# Walk the AST and parse the BINARY_OPERATOR/UNARY_OPERATOR
for node in func_decl.walk_preorder():
    if node.kind == CursorKind.BINARY_OPERATOR:
        left, op, right = split_binary_operator(node)
        print(
            f"BINARY_OP left: {print_tokens(left)}  op: {op}  right: {print_tokens(right)}",
        )
    elif node.kind == CursorKind.UNARY_OPERATOR:
        op, expr, pos = split_unary_operator(node)
        print(f"UNARY_OP op: {op}  expr: {print_tokens(expr)}  position: {pos}")
