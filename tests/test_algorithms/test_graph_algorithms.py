from PyBirdViewCode.algorithms import graph_algorithms
from PyBirdViewCode import FileManager
from tests.base import asset_path
import networkx as nx


def test_graph_alg():
    path = asset_path("graph-alg-utils")
    cfg = FileManager(path).dot_load("cfg.dot", False)
    assert isinstance(cfg, nx.MultiDiGraph)
    cfg = nx.DiGraph(cfg)
    entry, exit = graph_algorithms.get_entry_and_exit(cfg)
    assert entry == "1"
    assert exit == "2"


def test_nx_ordered_op():
    G = nx.DiGraph()
    G.add_edge(1, 2)
    G.add_edge(1, "entry")
    G.add_edge(1, 4)
    assert list(G.out_edges(1)) == [(1, 2), (1, "entry"), (1, 4)]
    assert list(G.neighbors(1)) == [2, "entry", 4]

    graph_algorithms.update_out_edge_with_order(G, 1, "entry", "exit")

    assert list(G.out_edges(1)) == [(1, 2), (1, "exit"), (1, 4)]

    graph_algorithms.update_out_edge_with_order(G, 1, 4, "mynode")

    assert list(G.out_edges(1)) == [(1, 2), (1, "exit"), (1, "mynode")]
