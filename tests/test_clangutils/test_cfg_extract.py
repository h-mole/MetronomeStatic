from MetronomeStatic.third_parties.cfg_extractor.decorators.concrete_node_decorators import (
    ifStmt,
)
from MetronomeStatic.third_parties.cfg_extractor import build_cfg, SkyCFG
from MetronomeStatic.clang_utils import beautified_print_ast
from tests.base import asset_path
import networkx as nx
from MetronomeStatic.third_parties.cfg_extractor.decorators import *


def test_cfg_extraction():
    cfg = build_cfg(asset_path("cfg-extract/cfg-demo.c"), "goto_structure")

    nx.nx_pydot.write_dot(cfg, "cfg-demo.dot")
