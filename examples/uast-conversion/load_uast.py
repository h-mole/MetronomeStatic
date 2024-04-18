import json

from MetronomeStatic import universal_ast_nodes as nodes


# 从json文件中加载AST
with open("dumped-ast.json", "r") as f:
    ast = nodes.SourceElement.from_dict(json.load(f))
    print(ast)
