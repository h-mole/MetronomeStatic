from MetronomeStatic.joern_utils import parse_cpg_dot, pydot_to_nx
from tests.base import asset_path


def test_parse_ddg():
    dot_file = asset_path("joern-cpg-dots/wrong.dot")

    # 使用词法分析器和语法分析器解析输入文件
    with open(dot_file, "r") as f:
        data = f.read()

    result = parse_cpg_dot(data)
    assert len(result) == 1
    # cpg_dot_to_network(result[0])
    pydot_to_nx(result[0])
