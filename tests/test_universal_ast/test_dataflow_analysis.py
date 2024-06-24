import os
from PyBirdViewCode.clang_utils.code_attributes.utils import get_func_decl, parse_file
from PyBirdViewCode.uast.c_cpp_converter import ClangASTConverter
from PyBirdViewCode.uast.universal_cfg_extractor import CFGBuilder
from PyBirdViewCode.uast.universal_dataflow_analysis import analyse
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
    # analyse(cfg)
    # cfg.topology
    # print(cfg.topology.no)
    doms = nx.immediate_dominators(cfg.topology, cfg.entry_block.block_id)   
    print(doms)