import sys

sys.path.append("../../")
import networkx as nx
from PyBirdViewCode.clang_utils import *

# from PyBirdViewCode
from PyBirdViewCode import (
    universal_ast_nodes as nodes,
    ClangASTConverter,
    CFGBuilder,
    FileManager,
    CodePropertyGraphs
)

fm = FileManager(".")
# 获取 Clang AST 的Cursor对象
file_cursor = parse_file("demo.c").cursor

# 获取函数main的Cursor对象
cursor = get_func_decl(file_cursor, "main")

# 获取UAST
ast = ClangASTConverter().eval(cursor)

# 使用CFGBuilder构建CFG
cfg_builder = CFGBuilder()
cfg = cfg_builder.build(ast)

# 将CFG转换为networkx的网络，并且保存为dot
g = cfg.to_networkx()
fm.dot_dump(
    "cfg.dot",
    g,
)



# 得到.dot文件之后，可以用dot转化cfg.dot为图片
os.system("dot -Tpng cfg.dot -o cfg.png")

# 从cfg中抽取代码属性图
cpgs = CodePropertyGraphs.create(cfg)

# 控制依赖图（CDG）
fm.dot_dump(
    "cdg.dot",
    cpgs.cdg_nx,
)
# 转化为图片
os.system("dot -Tpng cdg.dot -o cdg.png")

# 数据依赖图（DDG）
fm.dot_dump(
    "ddg.dot",
    cpgs.ddg_nx,
)
# 转化为图片
os.system("dot -Tpng ddg.dot -o ddg.png")

# 程序依赖图（PDG）
fm.dot_dump(
    "pdg.dot",
    cpgs.pdg_nx,
)
# 转化为图片
os.system("dot -Tpng pdg.dot -o pdg.png")
