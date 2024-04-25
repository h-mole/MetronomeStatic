from typing import Dict, Iterable, List, Optional, Tuple
import networkx as nx
from MelodieFuncFlow import MelodieGenerator

# 一个基础块有其id，为一个字符串；每一个基础块中可能含有多个变量的定义
# 由于基础块中变量定义是有序的，因此每一个基础块中的变量定义，可以保存在一个列表中
# 由此，通过基础块号(str)与变量定义语句在此基础块中的顺序(int)组成的tuple，就可以唯一确定一个变量定义语句
DEF_ID = Tuple[str, int]


class ReachingDefinitionAnalysis:
    """
    zh:

    :field cfg: 控制流图的图结构。节点为基本块的序号，建议使用字符串作为节点id
        cfg只要图结构即可，无需节点和边的属性
    :definitions: 定义集合，key为基本块的序号，value为基本块中定义的变量列表
        key要和cfg的节点id保持一致
    """

    class NodeStatus:
        """
        zh:

        :field node: 节点id
        :field gens: 该节点内包含的变量赋值语句，包含的为True，否则为False
        :field kills: 该节点内，哪一个语句对变量的赋值会被覆盖，会被覆盖为True，否则False
        :field output: 该节点的输出，表示相应语句产生的变量值是否会到达该节点的输出端
        """

        def __init__(self, node: str, all_var_defs: Iterable[DEF_ID]):
            self.node = node
            self.gens: Dict[DEF_ID, bool] = {}
            self.kills: Dict[DEF_ID, bool] = {}
            self.output: Dict[DEF_ID, bool] = {}
            for var_def in all_var_defs:
                self.output[var_def] = self.gens[var_def] = self.kills[var_def] = False

        def bool_dict_difference(
            self, d1: Dict[DEF_ID, bool], d2: Dict[DEF_ID, bool]
        ) -> Dict[DEF_ID, bool]:
            """
            zh:

            差集运算
            """
            new_dict = {k: False for k in d1.keys()}
            for k in d1.keys():
                new_dict[k] = d1[k] and not d2[k]
            return new_dict

        def bool_dict_pair_difference(
            self, d1: Dict[DEF_ID, bool], d2: Dict[DEF_ID, bool]
        ) -> Dict[DEF_ID, bool]:
            """
            zh:

            并集运算
            """
            new_dict = {k: False for k in d1.keys()}
            for k in d1.keys():
                new_dict[k] = d1[k] or d2[k]
            return new_dict

        def bool_dicts_union(
            self, inputs: List[Dict[DEF_ID, bool]]
        ) -> Dict[DEF_ID, bool]:
            """
            zh:

            输入多个字典，并求其并集
            """
            first_input = inputs[0]
            union = first_input
            for item in inputs[1:]:  # 优化
                union = self.bool_dict_pair_difference(union, item)
            return union

        def iterate_single_step(self, inputs: List[Dict[DEF_ID, bool]]):
            """
            zh:

            迭代一步，根据前驱节点的输出，计算当前节点的输出
            """
            # 如果有前驱节点
            if len(inputs) > 0:
                input = self.bool_dicts_union(inputs)
            # 如果没有前驱节点，那么就构造一组全False的输入
            else:
                input = {k: False for k in self.gens.keys()}

            mid_result = self.bool_dict_difference(input, self.kills)
            return self.bool_dict_pair_difference(self.gens, mid_result)

        def __repr__(self) -> str:
            return f"NodeStatus(node={self.node}, gens={self.gens}, kills={self.kills})"

    def __init__(
        self,
        cfg: nx.DiGraph,
        defs: Dict[str, List[str]],
    ) -> None:
        self.cfg = cfg
        self.defs = defs
        start_nodes = (
            MelodieGenerator(cfg.nodes).filter(lambda x: cfg.in_degree(x) == 0).l
        )
        end_nodes = (
            MelodieGenerator(cfg.nodes).filter(lambda x: cfg.out_degree(x) == 0).l
        )
        assert len(start_nodes) == 1
        assert len(end_nodes) == 1
        self.start_node: str = start_nodes[0]
        self.end_node: str = end_nodes[0]

        # 保存所有基础块的名字，主要目的是保持顺序，避免字典乱序导致结果错误
        self.basic_block_names = list(self.cfg.nodes)

        self.all_var_defs = [
            (node, var_def_index)
            for node in self.basic_block_names
            for var_def_index in range(len(self.defs[node]))
        ]
        self.bb_status = {
            node: self.NodeStatus(node, self.all_var_defs)
            for node in self.basic_block_names
        }

        self._init_nodes_status()
        print(self.bb_status)
        self._last_status = None

    def run(self):
        self.iterate()
        return self

    def iterate_finish(self):
        """
        判断迭代是否已经完成，也就是说，各个节点的输出与上次迭代的结果是否不再变化
        只要不再变化，则返回True
        """
        values = []
        for bb in self.basic_block_names:
            for define_id in self.all_var_defs:
                var_def = self.bb_status[bb].output[define_id]
                values.append(var_def)
        iterate_status = tuple(values)
        print(hash(iterate_status), hash(self._last_status))
        if self._last_status is not None and self._last_status == iterate_status:
            return True
        else:
            self._last_status = iterate_status
            return False

    def iter_step_update_bb_outputs(self):
        for bb in self.basic_block_names:
            predecessor_bb_outputs = [
                self.bb_status[node].output for node in self.cfg.predecessors(bb)
            ]
            self.bb_status[bb].output = self.bb_status[bb].iterate_single_step(
                predecessor_bb_outputs
            )

    def iterate(self):
        while 1:
            if self.iterate_finish():
                break
            self.iter_step_update_bb_outputs()

    def _init_nodes_status(self):
        """
        输入多个节点，初始化每个节点的输出
        """
        for basic_block_name in self.basic_block_names:
            for var_def_index, var_defined in enumerate(self.defs[basic_block_name]):
                self.bb_status[basic_block_name].gens[
                    (basic_block_name, var_def_index)
                ] = True
                for basic_block_name_inner in self.basic_block_names:
                    if basic_block_name != basic_block_name_inner:

                        for var_defined_inner_index, var_defined_inner in enumerate(
                            self.defs[basic_block_name_inner]
                        ):
                            # 如果有相同的变量定义，则判断此节点注销了定义
                            if var_defined_inner == var_defined:
                                self.bb_status[basic_block_name].kills[
                                    (basic_block_name_inner, var_defined_inner_index)
                                ] = True

    def get_bb_output(self, bb_id: str) -> Dict[DEF_ID, bool]:
        """
        zh:
        
        反映了各个语句的赋值可否到达该基础块的出口

        :bb_id: 要查询的基础块的id

        """
        return self.bb_status[bb_id].output

    def get_bb_input(self, bb_id: str) -> Dict[DEF_ID, bool]:
        """
        zh:
        
        :bb_id: 要查询的基础块的id

        如果``bb_id='B2'``，返回的结果是:
        ```python
        {
            ('B1', 0): True, ('B1', 1): True, ('B1', 2): True, 
            ('B2', 0): True, ('B3', 0): True, ('B4', 0): False, 
            ('B4', 1): True, ('B5', 0): True, ('B6', 0): False
        }
        ```
        那么就说明基础块B1中索引为0、1、2的语句，B2中索引为0的语句等产生的变量值，均可能到达B2基础块的入口；
        基础块B4、B6中索引为0的语句，产生的变量值到不了B2基础块的入口

        """
        predecessor_bb_outputs = [
            self.bb_status[node].output for node in self.cfg.predecessors(bb_id)
        ]
        return self.bb_status[bb_id].bool_dicts_union(predecessor_bb_outputs)

    def format_bool_dict(
        self, bool_dic: Dict[DEF_ID, bool], nodes_order: Optional[List[str]] = None
    ) -> List[bool]:
        """
        按基础块顺序，将字典中所有定义语句后的布尔值写入到一个列表中
        """
        if nodes_order is None:
            nodes_order = self.basic_block_names
        keys = []
        for node in nodes_order:
            for def_id in range(len(self.defs[node])):
                key = (node, def_id)
                keys.append(key)
        return [bool_dic[key] for key in keys]


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
    analysis = ReachingDefinitionAnalysis(G, defs).run()
    for node, status in analysis.bb_status.items():
        print(node, status.output)
    print("b2-output", analysis.get_bb_output("B2"))
    print("b2-input", analysis.get_bb_input("B2"))
    print("b2-input", analysis.format_bool_dict(analysis.get_bb_input("B2")))
