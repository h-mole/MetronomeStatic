import os
from PyBirdViewCode.algorithms.reaching_definition import VarDefItem
from PyBirdViewCode.algorithms.domination_analysis import (
    get_forward_dominance_tree,
    merge_cfg_and_fdt,
)
from PyBirdViewCode.clang_utils.code_attributes.utils import get_func_decl, parse_file
from PyBirdViewCode import ClangASTConverter
from PyBirdViewCode.uast import (
    CFGBuilder,
    remove_empty_node_from_cfg,
    get_ddg_topology,
    get_cdg_topology,
)

from PyBirdViewCode.uast.universal_dataflow_analysis import rda_on_cfg
from PyBirdViewCode.utils.files import FileManager
from PyBirdViewCode import abspath_from_file
from tests.base import asset_path
import networkx as nx

fm = FileManager(
    abspath_from_file(
        "output",
        __file__,
    )
)


def test_data_flow_analysis():
    file = asset_path("universal-ast-extraction/dataflow-demo.c")
    evaluator = ClangASTConverter()
    cursor = get_func_decl(
        parse_file(
            file,
        ).cursor,
        "demo1",
    )
    assert cursor is not None

    ret = evaluator.eval(cursor)
    print(ret)
    cb = CFGBuilder()
    cfg = cb.build(ret)

    print(cfg.print_graph())

    graph = cfg.to_networkx()
    fm.dot_dump(graph, "dataflow-demo-cfg.dot")

    fm.dot_dump(cfg.to_networkx(), "cfg_purged.dot")

    ddg = get_ddg_topology(cfg, ["x", "y", "z"])
    fm.dot_dump(ddg, "ddg.dot")

    # fdt = get_forward_dominance_tree(cfg.topology, cfg.exit_block.block_id)
    merged = get_cdg_topology(cfg)
    pdg = nx.DiGraph()
    for node_id in merged.nodes:
        if node_id != "CDG_ENTRY":
            merged.nodes[node_id]["label"] = graph.nodes[node_id]["label"]
    fm.dot_dump(merged, "cdg.dot")
    pdg: nx.DiGraph = nx.compose(merged, ddg)
    pdg.remove_node("CDG_ENTRY")
    fm.dot_dump(pdg, "pdg.dot")

    # slicing
    # criteria: var z, line 15
    for node in cfg.topology.nodes:
        if len(cfg.get_block(node).statements) > 0:
            stmt = cfg.get_block(node).statements[0]
            if stmt.location[0] == 15:
                # stmt.
                break
