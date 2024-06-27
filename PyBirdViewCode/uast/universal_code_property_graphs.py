import networkx as nx

from .universal_cfg_extractor import CFG
from ..algorithms import get_forward_dominance_tree, merge_cfg_and_fdt
from .universal_dataflow_analysis import dataflow_analyse


class CodePropertyGraphs:
    def __init__(self, cfg: CFG) -> None:
        self._cfg = cfg
        self.cfg_nx = cfg.to_networkx()
        self.cdg_nx = get_cdg_topology(self._cfg)
        self.ddg_nx = get_ddg_topology(self._cfg)
        self.pdg_nx = compose_pdg_topology(self.cdg_nx, self.ddg_nx)
        # self.cfg_nx
        list(map(self.add_label, [self.cdg_nx, self.ddg_nx, self.pdg_nx]))

    def add_label(self, g: nx.DiGraph):
        for node in g.nodes:
            
            if node != "CDG_ENTRY":
                g.nodes[node]["label"] = self.cfg_nx.nodes[node].get("label", f"#{node}")

    @classmethod
    def create(cls, cfg: CFG):
        return cls(cfg)


def get_cdg_topology(cfg: CFG):
    """
    创建CDG的拓扑结构
    """
    fdt = get_forward_dominance_tree(cfg.topology)
    cdg = merge_cfg_and_fdt(cfg.topology, fdt).reverse()
    return cdg


def get_ddg_topology(cfg: CFG):
    """
    创建DDG的拓扑结构
    """
    result, var_refs = dataflow_analyse(cfg)
    ddg_topology = nx.DiGraph()
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
                    ddg_topology.add_edge(
                        node_id, var_def.node_id, label=referenced_var
                    )

            print(valid_vars)

    return ddg_topology


def compose_pdg_topology(cdg: nx.DiGraph, ddg: nx.DiGraph):
    """
    创建PDG的拓扑结构
    """

    pdg: nx.DiGraph = nx.compose(cdg, ddg)

    return pdg


def get_code_property_graphs(cfg: CFG):
    """
    输入一个CFG，也同时返回DDG、CDG和PDG
    """
