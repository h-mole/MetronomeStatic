import networkx as nx
from MelodieFuncFlow import MelodieGenerator


def get_forward_dominance_tree(cfg_topology: nx.DiGraph):
    """
    获取CFG拓扑结构的前向支配树

    由于构建FDT无需用到具体语句的信息，因此该函数只接收CFG的拓扑结构即可。

    :cfg_topology: CFG的拓扑结构
    """
    reversed = cfg_topology.reverse()
    dom_tree = nx.DiGraph()

    # 获取CFG拓扑结构的出口节点
    end_nodes = list(
        filter(lambda node: cfg_topology.out_degree(node) == 0, cfg_topology.nodes)
    )
    assert len(end_nodes) == 1
    cfg_end_node = end_nodes[0]

    # 遍历直接支配节点列表，重新构建支配树
    for node, immediate_dominator in nx.immediate_dominators(
        reversed, cfg_end_node
    ).items():
        if node != immediate_dominator:
            dom_tree.add_edge(immediate_dominator, node)
    return dom_tree


def merge_cfg_and_fdt(cfg_topology: nx.DiGraph, fdt: nx.DiGraph) -> nx.DiGraph:
    """
    CFG拓扑结构（以下简称为CFG）和FDT的节点构成相同。
    要构建CDG，就必须将CFG和FDG这两个图进行融合。

    具体融合规则为：两图的各个有向边取并集；方向相反的有向边互相抵消。

    生成的CDG的根节点名称为`ENTRY`

    :cfg_topology: ....
    """
    new_graph = nx.DiGraph()
    # 先将CFG的所有边加入
    for u, v in cfg_topology.edges():
        new_graph.add_edge(u, v)
    for u, v in fdt.edges():
        # 如果CFG中存在和FDT的当前边(u, v)相反的边(v, u)
        # 则删除这条反向边(v, u)
        # 否则正常增加边
        if new_graph.has_edge(v, u):
            new_graph.remove_edge(v, u)
        # else:
    # 寻找所有入度=0的节点
    # 然后创建一个CDG入口节点，链接这些所有的节点
    dangling_nodes = (
        MelodieGenerator(new_graph.nodes)
        .filter(lambda n: new_graph.in_degree(n) == 0)
        .l
    )
    new_graph.add_node("ENTRY")
    for dangling_node in dangling_nodes:
        new_graph.add_edge("ENTRY", dangling_node)
    return new_graph
