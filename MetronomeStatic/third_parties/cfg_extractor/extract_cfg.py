from dataclasses import dataclass
import networkx as nx
from .utils import buildCFG, CFG
from typing import Any, List, Mapping, Optional, Tuple, TypedDict, Union
from clang.cindex import Cursor
from .cfgblock import PredicateKinds


@dataclass
class CFGNodeData:
    stmts: List[Cursor]
    predicate: Optional[Tuple[PredicateKinds, Cursor]]


@dataclass
class CFGEdgeData:
    value: Union[bool, str, None]


class SkyCFG(nx.DiGraph):
    def __init__(self, incoming_graph_data=None, **attr):
        super().__init__(incoming_graph_data, **attr)
        self.start_node: int = -1
        self.end_node: int = -1

    def get_node_data(self, node_id: int) -> CFGNodeData:
        return self.nodes[node_id]["data"]

    def get_edge_data(self, u: int, v: int) -> CFGEdgeData:
        return self.edges[(u, v)]["data"]

    @classmethod
    def from_pyc_cfg(cls, cfg: CFG) -> "SkyCFG":
        nx_cfg = cls()
        for b in cfg._blocks.begin():
            block_id = b.getBlockID()
            stmts = [
                "".join([t.spelling for t in stmt.get_tokens()])
                for stmt in b.get_statements()
            ]
            nx_cfg.add_node(
                block_id,
                label=(
                    f"#{block_id} {set([cls.location().line for cls in b._elements.vector()])}  "
                    + f"{b._predicate[0] if b._predicate is not None else ''} {''.join([t.spelling for t in b._predicate[1].get_tokens()]) if b._predicate is not None else ''}"
                    + f"{stmts}"
                ),
                data=CFGNodeData(
                    stmts=list(b.get_statements()),
                    predicate=b._predicate,
                ),
            )

        for b in cfg._blocks.begin():
            block_id = b.getBlockID()
            for pred in b.pred_begin():
                edge = (pred.getReachableBlock().getBlockID(), block_id)
                if edge not in nx_cfg.edges:
                    nx_cfg.add_edge(*edge)
            for i, succ in enumerate(b.succs_begin()):
                edge_data = CFGEdgeData(None)
                if b._predicate is not None and b._predicate[0] == "if":
                    edge_data.value = True if i == 0 else False
                nx_cfg.add_edge(
                    block_id,
                    succ.getReachableBlock().getBlockID(),
                    label=edge_data.value,
                    data=edge_data,
                )
        nx_cfg.start_node = next(
            filter(lambda n: nx_cfg.in_degree(n) == 0, nx_cfg.nodes)
        )
        nx_cfg.end_node = next(
            filter(lambda n: nx_cfg.out_degree(n) == 0, nx_cfg.nodes)
        )
        return nx_cfg


def build_cfg(file: str, function: str) -> SkyCFG:
    cfg = buildCFG(file, function)
    return SkyCFG.from_pyc_cfg(cfg)
