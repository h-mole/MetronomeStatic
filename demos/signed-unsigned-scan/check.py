import json
import sys
import time

from MetronomeStatic.clang_utils import *
from MetronomeStatic.utils.service import Position, Problem


def find_hidden_conversions(node: Cursor) -> bool:
    """
    node需要是一个表达式。
    """
    has_unsigned = False
    has_signed = False

    def callback(ctx: TraversalContext):
        nonlocal has_unsigned, has_signed
        print(ctx.current_node.type.spelling)
        if ctx.current_node.type.spelling.startswith("unsigned"):
            has_unsigned = True
        if not ctx.current_node.type.spelling.startswith("unsigned"):
            has_signed = True

    traversal_with_callback(node, callback)
    return has_unsigned and has_signed


def check_signed_unsigned(node: Cursor):
    left, op, right = split_binary_operator(node)
    if op == "/":
        if left.type.spelling.startswith("unsigned"):
            has_hidden_conv_l = find_hidden_conversions(left)
            has_hidden_conv_r = find_hidden_conversions(right)

            if has_hidden_conv_l or has_hidden_conv_r:
                loc: cindex.SourceLocation = (
                    left if has_hidden_conv_l else right
                ).location
                log = "存在从有符号型整数到无符号型整数的隐式转换，可能存在类型问题。"
                # log = log.format(position=f"{loc.file}:{loc.line} column:{loc.column}")
                # self.current_context.found_problems.append(
                return Problem(
                    file=loc.file.name,
                    description=log,
                    position=Position.line_col(loc.line, loc.column),
                )
                # )


def check(file_name: str):
    problems = (
        iter_ast_from_file(file_name)
        .filter(lambda c: c.kind == CursorKind.BINARY_OPERATOR)
        .map(check_signed_unsigned)
        .filter(lambda item: item is not None)
        .cast(Problem)
        .map(lambda item: item.to_json())
        .l
    )

    with open("problems.json", "w") as f:
        json.dump(problems, f, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    file = sys.argv[1]
    time.sleep(3)
    check(file)
