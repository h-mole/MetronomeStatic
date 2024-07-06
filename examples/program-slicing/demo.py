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

# 程序依赖图（PDG）
fm.dot_dump(cpgs.pdg_nx, "pdg.dot", export_png=True)
