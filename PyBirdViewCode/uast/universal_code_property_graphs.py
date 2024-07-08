import networkx as nx
from .universal_ast_nodes import MethodDecl
from .universal_cfg_extractor import CFG, CFGBuilder
from ..algorithms import (
    get_forward_dominance_tree,
    merge_cfg_and_fdt,
    build_control_dependence_graph,
)
from .universal_dataflow_analysis import rda_on_cfg
from .uast_queries import UASTQuery


def add_label(cfg_nx: nx.DiGraph, g: nx.DiGraph):
    for node in g.nodes:

        if node != "ENTRY":
            g.nodes[node]["label"] = cfg_nx.nodes[node].get("label", f"#{node}")


class CodePropertyGraphs:
    def __init__(
        self, func_or_method_uast: MethodDecl, extra_variables: list[str]
    ) -> None:
        self._cfg = CFGBuilder().build(func_or_method_uast)
        self._extra_variables = extra_variables
        self.cfg_nx = self._cfg.to_networkx()
        self.cdg_nx = get_cdg_topology(self._cfg)
        self.ddg_nx = get_ddg_topology(
            self._cfg,
            [param.name.id for param in UASTQuery.get_all_params(func_or_method_uast)]
            + self._extra_variables,
        )
        self.pdg_nx = compose_pdg_topology(self.cdg_nx, self.ddg_nx)
        list(
            map(
                lambda g: add_label(self.cfg_nx, g),
                [self.cdg_nx, self.ddg_nx, self.pdg_nx],
            )
        )


def get_pdg_from_cfg(cfg: CFG, params: list[str], extra_variables: list[str]):
    """
    从CFG中抽取PDG
    """
    cfg_nx = cfg.to_networkx()
    cdg_nx = get_cdg_topology(cfg)
    ddg_nx = get_ddg_topology(
        cfg,
        [param for param in params] + extra_variables,
    )
    pdg_nx = compose_pdg_topology(cdg_nx, ddg_nx)
    add_label(cfg_nx, pdg_nx)
    return pdg_nx


def get_cdg_topology(cfg: CFG):
    """
    创建CDG的拓扑结构
    """
    # fdt = get_forward_dominance_tree(cfg.topology)
    # cdg = merge_cfg_and_fdt(cfg.topology, fdt).reverse()
    return build_control_dependence_graph(cfg.topology)


def get_ddg_topology(cfg: CFG, arg_variables: list[str]):
    """
    创建DDG的拓扑结构
    """
    result, var_refs = rda_on_cfg(cfg, arg_variables)
    ddg_topology = nx.DiGraph()
    for node_id, vars_ref in var_refs.items():
        for referenced_var in vars_ref:
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
