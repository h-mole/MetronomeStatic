from typing import Dict, List
from PyBirdViewCode.algorithms import reaching_definition_analysis, bool_list_to_str
from PyBirdViewCode.algorithms.reaching_definition import RDAOp, RDAOpList
import networkx as nx
from PyBirdViewCode import FileManager, abspath_from_file
from PyBirdViewCode.algorithms.domination_analysis import get_forward_dominance_tree, merge_fdt_and_cfg

fm = FileManager(
    abspath_from_file(
        "./output",
        __file__,
    )
)


def test_dominator():
    G = nx.DiGraph()

    G.add_edges_from([(1, 2), (2, 3), (2, 4), (3, 5), (4, 5), (5, 6)])

    fdt = get_forward_dominance_tree(G)
    fm.dot_dump(
        "fdt.dot",
        fdt,
    )
    merged = merge_fdt_and_cfg(G, fdt)
    fm.dot_dump(
        "cdg.dot",
        merged,
    )