import networkx as nx
from MetronomeStatic.clang_utils import *
from MetronomeStatic import universal_ast_nodes as nodes, ClangASTConverter, CFGBuilder


# 获取 Clang AST 的Cursor对象
file_cursor = parse_file("demo.c").cursor

# 获取函数main的Cursor对象
cursor = get_func_decl(file_cursor, "main")

# 获取UAST
ast = ClangASTConverter().eval(cursor)

# 使用CFGBuilder构建CFG
cfg_builder = CFGBuilder()
cfg_builder.build(ast)

# 将CFG转换为networkx的网络，并且保存为dot
# 得到.dot文件之后，可以用
#  `dot -Tpng cfg.dot -o cfg.png`转化cfg.dot为图片
g = cfg_builder.to_networkx()
nx.nx_pydot.write_dot(g, "cfg.dot")
