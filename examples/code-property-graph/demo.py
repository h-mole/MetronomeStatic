import sys

sys.path.append("../../")
from PyBirdViewCode.clang_utils import *

# from PyBirdViewCode
from PyBirdViewCode import (
    FileManager,
    extract_uast_from_file,
    extract_cpg_from_method,
    UASTQuery,
)

fm = FileManager(".")

file_uast = extract_uast_from_file("demo.c")
func_uast = UASTQuery(file_uast).get_method_by_name("main")

# 抽取代码属性图
cpgs = extract_cpg_from_method(func_uast)

fm.dot_dump(
    "cfg.dot",
    cpgs.cfg_nx,
)

# 得到.dot文件之后，可以用dot转化cfg.dot为图片
os.system("dot -Tpng cfg.dot -o cfg.png")

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
