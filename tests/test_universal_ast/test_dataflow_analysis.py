import os
from PyBirdViewCode.algorithms.reaching_definition import VarDefItem
from PyBirdViewCode.algorithms.domination_analysis import (
    get_forward_dominance_tree,
    create_cdg,
)
from PyBirdViewCode.clang_utils.code_attributes.utils import get_func_decl, parse_file
from PyBirdViewCode.uast.c_cpp_converter import ClangASTConverter
from PyBirdViewCode.uast.universal_cfg_extractor import (
    CFGBuilder,
    remove_empty_node_from_cfg,
    create_cdg_topology
)
from PyBirdViewCode.uast.universal_dataflow_analysis import dataflow_analyse
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
    fm.dot_dump("dataflow-demo-cfg.dot", graph)
    new_cfg = remove_empty_node_from_cfg(cfg)
    # return
    fm.dot_dump("cfg_purged.dot", new_cfg.to_networkx())
    # return
    cfg = new_cfg
    result, var_refs = dataflow_analyse(cfg)
    # print(result)
    ddg = nx.DiGraph()
    for node_id, vars_ref in var_refs.items():
        for referenced_var in vars_ref:
            print(node_id, referenced_var)
            valid_vars = result[node_id]
            for var_def, reachable in valid_vars.items():
                if (
                    referenced_var == var_def.modified_var
                    and reachable
                    and node_id != var_def.node_id
                ):
                    ddg.add_edge(node_id, var_def.node_id, label=referenced_var)

            print(valid_vars)

    for node_id in ddg.nodes:
        ddg.nodes[node_id]["label"] = graph.nodes[node_id]["label"]
    fm.dot_dump("ddg.dot", ddg)

    # fdt = get_forward_dominance_tree(cfg.topology, cfg.exit_block.block_id)
    merged = create_cdg_topology(cfg)
    pdg = nx.DiGraph()
    for node_id in merged.nodes:
        if node_id != "CDG_ENTRY":
            merged.nodes[node_id]["label"] = graph.nodes[node_id]["label"]
    fm.dot_dump("cdg.dot", merged)
    pdg: nx.DiGraph = nx.compose(merged, ddg)
    pdg.remove_node("CDG_ENTRY")
    fm.dot_dump("pdg.dot", pdg)

    # slicing
    # criteria: var z, line 15
    for node in cfg.topology.nodes:
        if len(cfg.get_block(node).statements)>0:
            stmt =  cfg.get_block(node).statements[0]
            if stmt.location[0]==15:
                # stmt.
                break
    # fm.dot_dump("fdt.dot", fdt)
    # for node_id, vardefs in result.items():

    #     VarDefItem(node_id)
