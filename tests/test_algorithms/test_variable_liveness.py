from typing import List
from PyBirdViewCode.algorithms import (
    bool_list_to_str,
    variable_liveness_analysis,
)

import networkx as nx


def test_1():

    edges = [
        ("entry", "B1"),
        ("B1", "B2"),
        ("B2", "B3"),
        ("B2", "B4"),
        ("B3", "B5"),
        ("B4", "B5"),
        ("B4", "B2"),
        ("B5", "exit"),
    ]
    G = nx.DiGraph()
    G.add_edges_from(edges)
    defs = {
        "entry": [],
        "B1": ["x", "y"],
        "B2": ["z"],
        "B3": ["q"],
        "B4": ["x", "m"],
        "B5": ["p"],
        "exit": [],
    }
    uses = {
        "entry": [],
        "B1": ["p", "q", "z"],
        "B2": ["m"],
        "B3": ["y", "p"],
        "B4": ["x", "q", "y"],
        "B5": ["z"],
        "exit": [],
    }
    output = variable_liveness_analysis(
        G, ["x", "y", "z", "p", "q", "m"], defs, uses, ["entry", "exit"]
    )
    print("活跃变量分析结果：", output)
    # inputs, outputs = reaching_definition_analysis(G, defs, ["entry", "exit"])
    # assert bool_list_to_str(outputs["B1"]) == "111000000"
    # assert bool_list_to_str(inputs["B1"]) == "000000000"
    # assert bool_list_to_str(inputs["B2"]) == "111110110"
    # assert bool_list_to_str(outputs["B2"]) == "011110110"
