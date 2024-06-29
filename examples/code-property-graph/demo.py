import sys

sys.path.append("../../")

# from PyBirdViewCode
from PyBirdViewCode import (
    FileManager,
    get_file_uast,
    get_method_cpg,
    UASTQuery,
)

# 在当前路径下创建FileManager对象
fm = FileManager(".")

# 获取文件的UAST
file_uast = get_file_uast("demo.c")

# 通过UASTQuery，获取函数的UAST
func_uast = UASTQuery.get_method(file_uast, "main")

# 抽取代码属性图
cpgs = get_method_cpg(func_uast)

# 控制流图 （CFG）
fm.dot_dump(cpgs.cfg_nx, "cfg.dot", export_png=True)

# 控制依赖图（CDG）
fm.dot_dump(cpgs.cdg_nx, "cdg.dot", export_png=True)

# 数据依赖图（DDG）
fm.dot_dump(cpgs.ddg_nx, "ddg.dot", export_png=True)

# 程序依赖图（PDG）
fm.dot_dump(cpgs.pdg_nx, "pdg.dot", export_png=True)
