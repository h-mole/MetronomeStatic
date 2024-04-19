import sys

sys.path.append("../../..")

from PyBirdViewCode.clang_utils import *
from PyBirdViewCode import *

path = abspath_from_current_file("assets/interactive_query.c", __file__)

"""
Code above is critical for running this example,
and not necessary when using in an interactive environment (IPython/Jupyter).

↓↓ JUST FOCUS ON THE FOLLOWING CODE! ↓↓
"""

ret = (
    iter_ast(parse_file(path).cursor)
    .filter(lambda c: c.kind == CursorKind.FUNCTION_DECL and c.spelling == "main")
    .head()
)

print(ret.kind, ret.spelling)
