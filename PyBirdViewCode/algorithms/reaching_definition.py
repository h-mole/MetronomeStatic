from dataclasses import dataclass
from dataclasses_json import DataClassJsonMixin
from typing import Dict, Generic, List, Tuple, TypeVar, NamedTuple
import networkx as nx
from .base import lists_of_bool_union, list_of_bool_pair_diff, list_of_bool_pair_union
from functools import cache, cached_property


@dataclass
class RDAOp(DataClassJsonMixin):
    """
    用在可达定义分析的单个操作

    比如一个赋值语句：`x = a + b`，表示为操作 RDAOp("x", ["a", "b"])

    如果是一个语句中涉及多个值的情形，如`x, y = get_values()`，应当将其写入多个赋值操作中：

    RDAOp("x", [])
    RDAOp("y", [])
    """

    defined_var: str = ""
    used_var: List[str] = None
    location: Tuple[int, int] = (-1, -1)  # line, column

    def __post_init__(self):
        if self.used_var is None:
            self.used_var = []

    @staticmethod
    def find_var_modification_in_list(var: str, lst: List["RDAOp"]) -> int:
        for i, op in enumerate(lst):
            if op.defined_var == var:
                return i
        return -1


@dataclass
class RDAOpList(DataClassJsonMixin):
    ops: List[RDAOp]

    def contains_var_modification(self, var: str) -> bool:
        for op in self.ops:
            if op.defined_var == var:
                return True
        return False


class VarDefItem(NamedTuple):
    node_id: str
    modified_var: str


def create_empty_vector(length: int) -> List[bool]:
    return [False] * length


def get_defs(
    defs: List[Tuple[str, int, str]],
    nodes_lists: Dict[str, RDAOpList],
    def_list: List[bool],
) -> Dict[VarDefItem, bool]:
    d = {}
    for i, reachable in enumerate(def_list):
        node_id, op_index, var = defs[i]
        d[VarDefItem(node_id, var)] = (
            reachable
        )
    return d


def reaching_definition_analysis(
    cfg: nx.DiGraph,
    defs: Dict[str, RDAOpList],
    ignored_basic_blocks: List[str] = [],
) -> Tuple[
    Dict[str, List[bool]], Dict[str, List[bool]], Dict[str, Dict[VarDefItem, bool]]
]:
    """
    zh:

    :cfg: 输入的cfg
    :defs: 各个基本块中定义的变量
    :ignored_basic_blocks: 忽略的节点

    输出：参数1和2为语句的变量定义可否到达每一个节点的输入/输出；
    参数3代表在每一个节点上，变量定义(类型为VarDefItem)能否到达该节点
    
    """
    bb_list = list(filter(lambda n: n not in ignored_basic_blocks, cfg.nodes))
    defs_list: List[Tuple[str, int, str]] = [
        (node, index, rda_op.defined_var)
        for node in bb_list
        for index, rda_op in enumerate(defs[node].ops)
    ]
    vector_length = len(defs_list)
    gens: Dict[str, List[bool]] = {
        bb_id: [_bb_id == bb_id for _bb_id, _2, _3 in defs_list] for bb_id in bb_list
    }
    kills: Dict[str, List[bool]] = {
        bb_id: [
            (_bb_id != bb_id and (defs[bb_id].contains_var_modification(var_name)))
            for _bb_id, _2, var_name in defs_list
        ]
        for bb_id in bb_list
    }
    print(kills)
    print(defs_list)
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
    input_vardefs_reachable = {}
    for node in defs.keys():
        print("node #", node)
        input_vardefs_reachable[node] = get_defs(defs_list, defs, inputs[node])

    return inputs, outputs, input_vardefs_reachable
