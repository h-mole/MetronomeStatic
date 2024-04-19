import json

from PyBirdViewCode.clang_utils import *
from PyBirdViewCode import *

# 获取 Clang AST 的Cursor对象
file_cursor = parse_file("uast-demo.c").cursor

# 获取函数main的Cursor对象
cursor = get_func_decl(file_cursor, "main")

# 使用ClangASTConverter将Cursor对象转换为UAST
converter = ClangASTConverter()
uast = converter.eval(cursor)
print(uast)

# 将UAST转换为JSON格式并保存到文件
with open("dumped-ast.json", "w") as f:
    json.dump(uast.to_dict(), f, indent=2, ensure_ascii=False)
