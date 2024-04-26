from typing import Dict, List, Tuple
import networkx as nx
from .base import lists_of_bool_union, list_of_bool_pair_diff, list_of_bool_pair_union


def create_empty_vector(length: int) -> List[bool]:
    return [False] * length


def reaching_definition_analysis(
    cfg: nx.DiGraph,
    defs: Dict[str, List[str]],
    ignored_basic_blocks: List[str] = [],
) -> Tuple[Dict[str, List[bool]], Dict[str, List[bool]]]:
    """
    zh:

    :cfg: 输入的cfg
    :defs: 各个基本块中定义的变量
    :ignored_basic_blocks: 忽略的节点
    """
    bb_list = list(filter(lambda n: n not in ignored_basic_blocks, cfg.nodes))
    defs_list: List[Tuple[str, int, str]] = [
        (node, index, var_name)
        for node in bb_list
        for index, var_name in enumerate(defs[node])
    ]
    vector_length = len(defs_list)
    gens: Dict[str, List[bool]] = {
        bb_id: [_bb_id == bb_id for _bb_id, _2, _3 in defs_list] for bb_id in bb_list
    }
    kills: Dict[str, List[bool]] = {
        bb_id: [
            (_bb_id != bb_id and var_name in defs[bb_id])
            for _bb_id, _2, var_name in defs_list
        ]
        for bb_id in bb_list
    }
    inputs: Dict[str, List[bool]] = {
        bb_id: create_empty_vector(vector_length) for bb_id in bb_list
    }
    outputs: Dict[str, List[bool]] = {
        bb_id: create_empty_vector(vector_length) for bb_id in bb_list
    }

    could_break = False
    last_tup = (None,)
    while True:
        # 一维列表，将各个节点的vector的值按顺序保存进去
        # 用于判断是否已经到达不动点
        values = []
        for bb_id in bb_list:
            predecessor_inputs = [
                outputs[pred_id]
                for pred_id in cfg.predecessors(bb_id)
                if pred_id not in ignored_basic_blocks
            ]
            if len(predecessor_inputs) == 0:
                input_vector = create_empty_vector(vector_length)
            else:
                input_vector = lists_of_bool_union(predecessor_inputs)
            inputs[bb_id] = input_vector
            outputs[bb_id] = list_of_bool_pair_union(
                gens[bb_id], list_of_bool_pair_diff(input_vector, kills[bb_id])
            )
            values.extend(outputs[bb_id])
        tup = tuple(values)
        # 当到达不动点之后
        # 推迟一个循环周期再跳出循环
        # 确保input更新完毕
        if could_break:
            break

        if tup == last_tup:
            could_break = True
        else:
            last_tup = tup

    return inputs, outputs


if __name__ == "__main__":

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
    defs = {
        "entry": [],
        "B1": ["x", "y", "z"],
        "B2": ["x"],
        "B3": ["y"],
        "B4": ["z", "y"],
        "B5": ["z"],
        "B6": ["z"],
        "exit": [],
    }
    reaching_definition_analysis(G, defs, ["entry", "exit"])
    # analysis = ReachingDefinitionAnalysis(G, defs).run()
    # for node, status in analysis.bb_status.items():
    #     print(node, status.output)
    # print("b2-output", analysis.get_bb_output("B2"))
    # print("b2-input", analysis.get_bb_input("B2"))
    # print("b2-input", analysis.format_bool_dict(analysis.get_bb_input("B2")))
