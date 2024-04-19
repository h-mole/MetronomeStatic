import json
import sys

sys.path.append("../../..")

from PyBirdViewCode import abspath_from_current_file
from PyBirdViewCode.clang_utils import parse_file, extract_ast, get_func_decl

# Load file by clang and get the translation unit
translation_unit = parse_file(abspath_from_current_file("assets/load_ast.c", __file__))

# Get the cursor from Translation Unit
cursor = translation_unit.cursor

# Get the function declaration of "main"
main_func = get_func_decl(cursor, "main")

# Extract the JSON representation of Clang AST
ast = extract_ast(main_func)

# Print AST
print(json.dumps(ast, indent=2))
