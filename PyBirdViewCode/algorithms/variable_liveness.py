from typing import Dict, List, Tuple
import networkx as nx
from .base import lists_of_bool_union


def variable_liveness_analysis(
    cfg: nx.DiGraph,
    vars: List[str],
    defs: Dict[str, List[str]],
    uses: Dict[str, List[str]],
    ignored_basic_blocks: List[str],
) -> Tuple[Dict[str, List[bool]], Dict[str, List[bool]]]:
    """
    存活变量分析
    """
    block_uses = {node: [(v in uses[node]) for v in vars] for node in cfg.nodes}
    block_defs = {node: [(v in defs[node]) for v in vars] for node in cfg.nodes}
    bb_in_vectors = {node: [False for _ in vars] for node in cfg.nodes}
    bb_out_vectors = {node: [False for _ in vars] for node in cfg.nodes}

    nodes_list = list(filter(lambda n: n not in ignored_basic_blocks, cfg.nodes))

    last_tuple = None
    could_break = False
    while True:
        output = []
        for bb in nodes_list:
            outs = [bb_in_vectors[neighbor] for neighbor in cfg.neighbors(bb)]
            if len(outs) == 0:
                bb_out = [False] * len(vars)
            else:
                bb_out = lists_of_bool_union(outs)
            bb_def = block_defs[bb]
            bb_use = block_uses[bb]
            bb_in = [
                bb_use[i] or (bb_out[i] and not bb_def[i]) for i in range(len(bb_use))
            ]
            bb_out_vectors[bb] = bb_out
            bb_in_vectors[bb] = bb_in
            output.extend(bb_in)

        tup = tuple(output)
        if could_break:
            break
        if tup == last_tuple:
            could_break = True
        else:
            last_tuple = tup

    return bb_in_vectors, bb_out_vectors


if __name__ == "__main__":

    # 示例
    cfg = nx.DiGraph()
    cfg.add_edges_from(
        [
            ("entry", "B1"),
            ("B1", "B2"),
            ("B2", "B3"),
            ("B2", "B4"),
            ("B3", "B5"),
            ("B4", "B5"),
            ("B4", "B2"),
            ("B5", "exit"),
        ]
    )
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
