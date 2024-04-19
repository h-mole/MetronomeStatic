import json
import sys

sys.path.append("../../..")

from PyBirdViewCode.clang_utils import *
from PyBirdViewCode import *

path = abspath_from_current_file("assets/uast-demo.c", __file__)

"""
Code above is critical for running this example,
and not necessary when using in an interactive environment (IPython/Jupyter).

↓↓ JUST FOCUS ON THE FOLLOWING CODE! ↓↓
"""


evaluator = ClangASTConverter()
cursor = get_func_decl(
    parse_file(
        path,
    ).cursor,
    "main",
)
assert cursor is not None

ret = evaluator.eval(cursor)

with open("./outputs/dumped-ast.json", "w") as f:
    json.dump(ret.to_dict(), f, indent=2, ensure_ascii=False)
