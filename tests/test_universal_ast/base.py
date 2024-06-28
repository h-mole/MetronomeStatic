from typing import List
from PyBirdViewCode.clang_utils.code_attributes.utils import parse_file
from PyBirdViewCode.uast import ClangASTConverter
from tests.base import asset_path
import networkx as nx


def extract_uast_from_c(file: str):
    file = asset_path(file)
    evaluator = ClangASTConverter()
    cursor = parse_file(
        file,
    ).cursor
    assert cursor is not None

    ret = evaluator.eval(cursor)
    return ret


def verify_topology(expected_edges: List[tuple[int, int]], graph: nx.DiGraph):
    expected_topology = nx.DiGraph(expected_edges)
    assert nx.is_isomorphic(expected_topology, graph)
