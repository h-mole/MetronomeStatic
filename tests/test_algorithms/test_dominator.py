from typing import Dict, List
from PyBirdViewCode.algorithms import reaching_definition_analysis, bool_list_to_str
from PyBirdViewCode.algorithms.reaching_definition import RDAOp, RDAOpList
import networkx as nx
from PyBirdViewCode import FileManager, abspath_from_file
from PyBirdViewCode.algorithms.domination_analysis import (
    get_forward_dominance_tree,
    merge_cfg_and_fdt,
    build_control_dependence_graph,
)

from tests.base import asset_path
from tests.test_universal_ast.base import verify_topology

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
        fdt,
        "fdt.dot",
    )
    assert set(fdt.edges) == set([(6, 5), (5, 4), (5, 3), (5, 2), (2, 1)])
    merged = merge_cfg_and_fdt(G, fdt)
    assert set(merged.edges) == {
        (2, 3),
        (2, 4),
        ("ENTRY", 1),
        ("ENTRY", 2),
        ("ENTRY", 5),
        ("ENTRY", 6),
    }
    fm.dot_dump(
        merged,
        "cdg.dot",
    )


def test_dom_multi_stmts():
    dot_file = asset_path(r"algorithms-demo\cdg_extraction_demo.dot")
    g: nx.DiGraph = fm.dot_load(dot_file)
    cdg = build_control_dependence_graph(g)
    fm.dot_dump(cdg, "cdg-new.dot", True)
    verify_topology(
        [
            ("ENTRY", "4"),
            ("ENTRY", "2"),
            ("ENTRY", "11"),
            ("ENTRY", "12"),
            ("4", "7"),
            ("7", "9"),
            ("7", "10"),
        ],
        cdg,
    )
