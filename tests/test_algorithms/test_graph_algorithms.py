from PyBirdViewCode.algorithms import graph_algorithms
from PyBirdViewCode import FileManager
from tests.base import asset_path
import networkx as nx


def test_graph_alg():
    path = asset_path("graph-alg-utils")
    cfg = FileManager(path).dot_load("cfg.dot")
    assert isinstance(cfg, nx.MultiDiGraph)
    cfg = nx.DiGraph(cfg)
    entry, exit = graph_algorithms.get_entry_and_exit(cfg)
    assert entry == "1"
    assert exit == "2"
