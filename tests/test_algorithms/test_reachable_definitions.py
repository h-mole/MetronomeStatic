from typing import Dict, List
from PyBirdViewCode.algorithms import reaching_definition_analysis, bool_list_to_str
from PyBirdViewCode.algorithms.reaching_definition import RDAOp, RDAOpList
import networkx as nx
from PyBirdViewCode import FileManager, abspath_from_file

fm = FileManager(
    abspath_from_file(
        "./output",
        __file__,
    )
)


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

    defs: Dict[str, RDAOpList] = {
        "entry": RDAOpList([]),
        "B1": RDAOpList([RDAOp("x"), RDAOp("y"), RDAOp("z")]),
        "B2": RDAOpList([RDAOp("x")]),
        "B3": RDAOpList([RDAOp("y")]),
        "B4": RDAOpList([RDAOp("z"), RDAOp("y")]),
        "B5": RDAOpList([RDAOp("z")]),
        "B6": RDAOpList([RDAOp("z")]),
        "exit": RDAOpList([]),
    }
    fm.dot_dump("rda-test1.dot", G)
    inputs, outputs, _= reaching_definition_analysis(G, defs, [])
    assert bool_list_to_str(outputs["B1"]) == "111000000"
    assert bool_list_to_str(inputs["B1"]) == "000000000"
    assert bool_list_to_str(inputs["B2"]) == "111110110"
    assert bool_list_to_str(outputs["B2"]) == "011110110"
