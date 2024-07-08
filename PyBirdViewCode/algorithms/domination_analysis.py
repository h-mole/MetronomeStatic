from collections import defaultdict
import networkx as nx
from MelodieFuncFlow import MelodieGenerator
from .graph_algorithms import graph_algorithms


def get_forward_dominance_tree(cfg_topology: nx.DiGraph, reverse=True):
    """
    获取CFG拓扑结构的前向支配树

    由于构建FDT无需用到具体语句的信息，因此该函数只接收CFG的拓扑结构即可。

    :cfg_topology: CFG的拓扑结构
    """
    if reverse:
        cfg_topology = cfg_topology.reverse()
    dom_tree = nx.DiGraph()

    # 获取反向后CFG拓扑结构的入口节点(该节点的名称为exit，但反向后就是入口了)
    cfg_entry_node = graph_algorithms.get_entry(cfg_topology)
    # 遍历直接支配节点列表，重新构建支配树
    for node, immediate_dominator in nx.immediate_dominators(
        cfg_topology, cfg_entry_node
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


def dominance_frontier(cfg, idom):
    """
    计算控制流图 cfg 的支配边界
    """

    # 初始化支配边界
    df = defaultdict(set)

    # 遍历每个节点,计算其支配边界
    for node in cfg.nodes:
        predecessors = list(cfg.predecessors(node))
        # print(predecessors)
        if len(predecessors) > 1:
            for p in predecessors:
                runner = p
                print(runner, type(runner), type(node), node, idom)
                # if node
                while runner != idom[node]:
                    df[runner].add(node)
                    runner = idom[runner]

    return df


def control_dependence_graph(G, dominance_frontier):
    """
    构建控制依赖图
    """
    cdg = nx.DiGraph()
    for node in G.nodes:
        for frontier_node in dominance_frontier[node]:
            if node != frontier_node:
                cdg.add_edge(frontier_node, node)
    return cdg


def build_control_dependence_graph(cfg: nx.DiGraph):
    """
    使用支配边界法构建控制依赖图

    https://blog.csdn.net/Dong_HFUT/article/details/121492818
    https://blog.csdn.net/Dong_HFUT/article/details/121510224?spm=1001.2014.3001.5501

    """
    original_entry, original_exit = graph_algorithms.get_entry_and_exit(cfg)
    reversed_cfg = cfg.reverse()
    reversed_cfg.add_edge("exit", "ENTRY")
    reversed_cfg.add_edge(original_entry, "ENTRY")
    reversed_cfg.add_edge("exit", original_exit)

    dominance_tree = get_forward_dominance_tree(reversed_cfg, False)

    dom = defaultdict()
    for src, dst in dominance_tree.edges:
        dom[dst] = src
    dominance_frontiers = dominance_frontier(reversed_cfg, dom)
    cdg = control_dependence_graph(cfg, dominance_frontiers)
    return cdg
