from typing import List
from PyBirdViewCode.algorithms import (
    reaching_definition_analysis,
    bool_list_to_str
)
import networkx as nx


def bool_list_to_str(bl: List[bool]):
    return "".join(["1" if item else "0" for item in bl])


def test_1():

    edges = [
        ("entry", "B1"),
        ("B1", "B2"),
        ("B2", "B3"),
        ("B2", "B4"),
        ("B3", "B5"),
        ("B4", "B5"),
        ("B5", "B6"),
        ("B5", "B2"),
        ("B6", "exit"),
    ]
    G = nx.DiGraph()
    G.add_edges_from(edges)
    defs = {
        "entry": [],
        "B1": ["x", "y", "z"],
        "B2": ["x"],
        "B3": ["y"],
        "B4": ["z", "y"],
        "B5": ["z"],
        "B6": ["z"],
        "exit": [],
    }
    inputs, outputs = reaching_definition_analysis(G, defs, ["entry", "exit"])
    assert bool_list_to_str(outputs["B1"]) == "111000000"
    assert bool_list_to_str(inputs["B1"]) == "000000000"
    assert bool_list_to_str(inputs["B2"]) == "111110110"
    assert bool_list_to_str(outputs["B2"]) == "011110110"
