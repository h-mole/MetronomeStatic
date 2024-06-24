import networkx as nx
from MelodieFuncFlow import MelodieGenerator


def get_forward_dominance_tree(cfg_topology: nx.DiGraph):
    reversed = cfg_topology.reverse()
    dom_tree = nx.DiGraph()
    for node, immediate_dominator in nx.immediate_dominators(reversed, 6).items():
        if node != immediate_dominator:
            dom_tree.add_edge(immediate_dominator, node)
    return dom_tree


def merge_fdt_and_cfg(cfg_topology: nx.DiGraph, fdt: nx.DiGraph):
    """
    zh:
    CFG拓扑结构（在该函数注释的以下部分简称为CFG）和FDT的节点构成相同。
    然后去除CFG中和FDG节点相同但方向相反的边
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
    dangling_nodes = MelodieGenerator(new_graph.nodes).filter(
        lambda n: new_graph.in_degree(n) == 0
    ).l
    new_graph.add_node("CDG_ENTRY")
    for dangling_node in dangling_nodes:
        new_graph.add_edge("CDG_ENTRY", dangling_node)
    return new_graph
