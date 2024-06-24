from typing import List
from .universal_cfg_extractor import CFG
from .unparser import BaseUASTUnparser
from ..uast import universal_ast_nodes as nodes
from ..algorithms import RDAOp, RDAOpList, reaching_definition_analysis


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

    defs: dict[str, RDAOpList] = {
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
    inputs, outputs = reaching_definition_analysis(G, defs, ["entry", "exit"])
    assert bool_list_to_str(outputs["B1"]) == "111000000"
    assert bool_list_to_str(inputs["B1"]) == "000000000"
    assert bool_list_to_str(inputs["B2"]) == "111110110"
    assert bool_list_to_str(outputs["B2"]) == "011110110"


def analyse(cfg: CFG):
    
    # return 
    unparser = BaseUASTUnparser()
    defs: dict[str, RDAOpList] = {}
    for node in cfg.topology.nodes:
        block = cfg.get_block(node)
        assigned_variables = []
        for stmt_index, stmt in enumerate(block.statements):
            match stmt:
                case nodes.Assignment():
                    assigned_variables.extend(
                        [
                            (stmt_index, unparser.unparse(lhs_item), lhs_item.location)
                            for lhs_item in stmt.lhs
                        ]
                    )

                case nodes.UnaryExpr(sign="++" | "--"):
                    assigned_variables.append(
                        (
                            stmt_index,
                            unparser.unparse(stmt.expression),
                            stmt.location,
                        )
                    )

        print(node, assigned_variables)

        # defs[node] = RDAOpList([])
        ops: List[RDAOp] = []
        for stmt_index_, assigned_var_name_, loc in assigned_variables:
            mod_index = RDAOp.find_var_modification_in_list(assigned_var_name_, ops)
            if mod_index != -1:
                ops.pop(mod_index)
            ops.append(RDAOp(assigned_var_name_, index_in_bb=stmt_index_, location=loc))
        defs[node] = RDAOpList(ops)

    print(defs)
    _, _2, var_defs_reachable = reaching_definition_analysis(
        cfg.topology,
        defs,
        [],
    )

    print(var_defs_reachable)