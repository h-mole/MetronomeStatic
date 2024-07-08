import copy
from html import escape
import uuid

from PyBirdViewCode.algorithms.domination_analysis import (
    get_forward_dominance_tree,
    merge_cfg_and_fdt,
)
from ..uast import universal_ast_nodes as nodes
from typing import Dict, List, Literal, Tuple, Union, Optional
import networkx as nx
from .exceptions import OnBreakStatement
from ..algorithms import ValidNodeKinds, graph_algorithms
from .unparser.base_unparser import BaseUASTUnparser

BlockKinds = Literal["normal", "conditional", "switch", "method_return"]
LoopControlKinds = Literal["break", "continue"]


class BasicBlockData:
    def __init__(
        self,
        id: ValidNodeKinds,
        statements: Optional[List[nodes.SourceElement]] = None,
        kind: BlockKinds = "normal",
    ):
        self._id = id
        self.statements = statements if statements is not None else []
        self.kind: BlockKinds = kind

    @property
    def block_id(self):
        return self._id

    def add_statement(self, statement: nodes.SourceElement):
        self.statements.append(statement)

    def __repr__(self) -> str:
        return f"<BasicBlock #{self._id} {self.statements}>"

    @classmethod
    def from_block(cls, block: "BasicBlock"):
        return BasicBlockData(
            block._id,
            block.statements,
            block.kind,
        )


class BasicBlock(BasicBlockData):
    def __init__(
        self,
        id: int,
        statements: List[nodes.SourceElement] | None = None,
        kind: BlockKinds = "normal",
        tag_on_empty="",
        next_blocks: Optional[List["BasicBlock"]] = None,
    ):
        super().__init__(id, statements, kind)
        self.tag_on_empty = tag_on_empty
        self.next_blocks: List[BasicBlock] = (
            next_blocks if next_blocks is not None else []
        )

    def set_tag_on_empty(self, tag: str):
        self.tag_on_empty = tag

    def text_on_empty(self):
        return f"<Block>" if self.tag_on_empty == "" else f"<{self.tag_on_empty}>"


class CFG:
    """
    控制流图
    """

    def __init__(self, all_blocks: List[BasicBlockData], topology: nx.DiGraph) -> None:
        self._block_id_map: Dict[ValidNodeKinds, BasicBlockData] = {
            block.block_id: block for block in all_blocks
        }
        self.topology = topology
        self._block_id_max = 0  # 节点号最大为多少，用来生成新节点id

    def add_block(self, block: BasicBlockData):
        self._block_id_map[block._id] = block
        self.topology.add_node(block._id)

    def add_edge(self, src: ValidNodeKinds, dst: ValidNodeKinds):
        self.topology.add_edge(src, dst)

    @property
    def entry_block(self):
        entry_id = graph_algorithms.get_entry(self.topology)
        return self._block_id_map[entry_id]

    @property
    def exit_block(self):
        exit_id = graph_algorithms.get_exit(self.topology)
        return self._block_id_map[exit_id]

    @classmethod
    def from_basic_blocks(cls, basic_blocks: List[BasicBlock]):
        topology = cls._calc_topology(basic_blocks)
        blocks_data = [BasicBlockData.from_block(block) for block in basic_blocks]
        return CFG(blocks_data, topology)

    @property
    def _all_blocks(self) -> List[BasicBlockData]:
        return list(self._block_id_map.values())

    # @property
    # def topology(self) -> nx.DiGraph:
    #     """
    #     The topology of graph.
    #     """
    #     return self._topology

    @staticmethod
    def _calc_topology(
        blocks: List[BasicBlock],
    ) -> nx.DiGraph:
        """
        Calculate the topology of the cfg.

        :return: a nx.DiGraph with same edges while nodes just contain theirs id.
        """
        g = nx.DiGraph()
        for block in blocks:
            g.add_node(block._id)
            if block.kind == "normal":
                for nb in block.next_blocks:
                    g.add_edge(block._id, nb._id)
            elif block.kind == "conditional":
                g.add_edge(
                    block._id, block.next_blocks[0].block_id, cond="true", label="true"
                )
                g.add_edge(
                    block._id,
                    block.next_blocks[1].block_id,
                    cond="false",
                    label="false",
                )
            elif block.kind == "switch":
                for i, nb in enumerate(block.next_blocks):
                    g.add_edge(block._id, nb._id, cond=i, label=f"case #{i+1}")
        return g

    def to_networkx(self, unparse=True):
        """
        Convert this CFG to a networkx graph
        """
        g = copy.deepcopy(self.topology)
        uast_unparser = BaseUASTUnparser()

        for block in self._all_blocks:
            label_base = f"#{block._id} {escape(block.kind)}\n"
            if len(block.statements) > 0:
                if unparse:
                    stmts = [uast_unparser.unparse(stmt) for stmt in block.statements]
                else:
                    stmts = [str(stmt) for stmt in block.statements]
                g.nodes[block._id]["label"] = (
                    '"' + label_base + escape("\n".join(stmts)) + '"'
                )
            else:
                g.nodes[block._id]["label"] = label_base
        return g

    def print_graph(self):
        print(self.topology.edges)

    def get_block(self, block_id: int):
        return self._block_id_map[block_id]

    def new_node_id(self):
        self._block_id_max += 1
        while self._block_id_max in self.topology.nodes:
            self._block_id_max += 1
        return self._block_id_max


class CFGBuilder:
    def __init__(self) -> None:
        self._current_id = 0
        self.all_blocks: List[BasicBlock] = []
        self.block = self.new_block()
        self.head_block = self.block
        self.return_block = self.new_block()
        self.return_block.kind = "method_return"

        # Goto edges are from "goto" node and to the label
        # The edges should add in the last step
        self.goto_edges: List[Tuple[BasicBlock, str]] = []
        # self.loop_control_edges: List[Tuple[BasicBlock, BasicBlock]] = []

        # Storing continue or Break statements to add
        self.loop_control_stmts: List[Tuple[LoopControlKinds, BasicBlock]] = []

    def _remove_block(self, block: BasicBlock) -> None:
        self.all_blocks.remove(block)

    def search_block_with_label(self, label: str) -> BasicBlock:
        """
        Search through all basic blocks, and get the first block with a label
        """
        for block in self.all_blocks:
            if (
                (len(block.statements) > 0)
                and isinstance(block.statements[0], nodes.Label)
                and (block.statements[0].name == label)
            ):
                return block
        raise ValueError(f"No block starts with label `{label}`")

    def add_goto_edges(self) -> None:
        for block, label in self.goto_edges:
            target_block = self.search_block_with_label(label)
            block.next_blocks.append(target_block)

    def add_loop_control_edges(
        self, block_end_loop: BasicBlock, block_loop_head: BasicBlock
    ) -> None:
        # Handle probable break
        while len(self.loop_control_stmts) > 0:
            kind, block_with_control_stmt = self.loop_control_stmts.pop()
            if kind == "break":
                block_with_control_stmt.next_blocks.append(block_end_loop)
            elif kind == "continue":
                block_with_control_stmt.next_blocks.append(block_loop_head)
            else:
                raise NotImplementedError(kind)

    # ---------- Graph management methods ---------- #

    def new_block(self, statement=None, kind: BlockKinds = "normal") -> BasicBlock:
        """
        Create a new block with a new id.

        Returns:
            A Block object with a new unique id.
        """
        self._current_id += 1
        block = BasicBlock(self._current_id, kind=kind)
        if statement is not None:
            block.add_statement(statement)
        self.all_blocks.append(block)
        return block

    def build(
        self,
        method_decl_uast: nodes.MethodDecl,
        remove_empty_nodes=True,
        ensure_single_stmt_each_node=True,
    ):
        assert isinstance(method_decl_uast, nodes.MethodDecl), method_decl_uast

        self.build_on_method_declaration(method_decl_uast)
        cfg = CFG.from_basic_blocks(self.all_blocks)
        if remove_empty_nodes:
            remove_empty_node_from_cfg(cfg)
        if ensure_single_stmt_each_node:
            expand_multi_stmt_nodes(cfg)
        return cfg

    def build_on_method_declaration(self, node: nodes.MethodDecl):
        assert node.body is not None
        self.build_on_block_or_stmt(node.body)

        # Append a to-return block if the return statement
        #   was not explicitly written.
        if len(self.block.next_blocks) == 0:
            self.block.next_blocks.append(self.return_block)
        self.add_goto_edges()

    def build_on_block_or_stmt(
        self, node: Union[nodes.BlockStmt, nodes.SourceElement]
    ) -> bool:
        """
        Returns if the control flow was interrupted
        """
        handler_dict = {
            nodes.IfThenElseStmt: self.build_on_if_then_else,
            nodes.ReturnStmt: self.build_on_return,
            nodes.ForStmt: self.build_on_for,
            nodes.WhileStmt: self.build_on_while,
            nodes.DoWhileStmt: self.build_on_do_while,
            nodes.GoToStmt: self.build_on_goto,
            nodes.BreakStmt: self.build_on_break,
            nodes.ContinueStmt: self.build_on_continue,
            nodes.SwitchStmt: self.build_on_switch,
            nodes.BlockStmt: self.build_on_block_or_stmt,
        }
        if isinstance(node, nodes.BlockStmt):
            for i, statement in enumerate(node.statements):
                cls = statement.__class__
                if cls in handler_dict:
                    ret = handler_dict[cls](statement)
                    if ret:
                        return True
                else:
                    self.block.add_statement(statement)
        else:
            cls = node.__class__
            if cls in handler_dict:
                ret = handler_dict[cls](node)
                if ret:
                    return True
            else:
                self.block.add_statement(node)
        return False

    def build_on_if_then_else(self, node: nodes.IfThenElseStmt) -> bool:
        # save the last block
        last_block = self.block

        # create the block after if-else branch structure
        endif_block = self.new_block()
        endif_block.tag_on_empty = "END_IF"

        # create condition block and append to the last block
        condition_block = self.new_block(node.predicate, kind="conditional")
        last_block.next_blocks.append(condition_block)

        # replace the current block with a newly created basic block
        self.block = true_block = self.new_block()
        condition_block.next_blocks.append(true_block)

        # Build on the true branch. If a break/goto/return/continue returned
        #  do not create edge to the endif block.
        control_flow_continue = not self.build_on_block_or_stmt(node.if_true)
        endif_reachable = False
        if control_flow_continue:
            self.block.next_blocks.append(endif_block)
            endif_reachable = True

        # replace the current block with a newly created basic block
        if node.if_false is not None:
            self.block = false_block = self.new_block()
            condition_block.next_blocks.append(false_block)
            control_flow_continue = not self.build_on_block_or_stmt(node.if_false)
            if control_flow_continue:
                self.block.next_blocks.append(endif_block)
                endif_reachable = True
        else:
            condition_block.next_blocks.append(endif_block)
            endif_reachable = True

        last_block.next_blocks.append(condition_block)

        # If endif is not reachable, just return
        #   and should not change current block.
        if endif_reachable:
            self.block = endif_block
        else:
            self._remove_block(endif_block)
        return False

    def build_on_switch(self, node: nodes.SwitchStmt) -> bool:
        # save the last block
        block_before = self.block

        # create the block after for loop structure
        block_end_switch = self.new_block()
        block_end_switch.tag_on_empty = "END_SWITCH"

        block_switch_head = self.new_block(node.expression, kind="switch")
        block_before.next_blocks.append(block_switch_head)

        # If no break was found in case body
        # just continue executing the next case.
        last_case_block: Optional[BasicBlock]
        should_exec_next_case, last_case_block = False, None

        for case in node.switch_cases:
            case_block = self.block = self.new_block()

            # If no break was found in case body
            # just continue executing the next case.
            if should_exec_next_case:
                assert last_case_block is not None
                last_case_block.next_blocks.append(case_block)

            block_switch_head.next_blocks.append(case_block)
            switch_break = self.build_on_block_or_stmt(case.body)
            if switch_break:
                self.block.next_blocks.append(block_end_switch)
                should_exec_next_case = False
                last_case_block = None
            else:
                should_exec_next_case = True
                last_case_block = self.block
        self.block = block_end_switch
        return False

    def build_on_while(self, node: nodes.WhileStmt) -> bool:
        # save the last block
        last_block = self.block

        # create the block after for loop structure
        block_end_loop = self.new_block()
        block_end_loop.tag_on_empty = "END_WHILE"

        if node.predicate is not None:
            block_loop_head = self.new_block(node.predicate, kind="conditional")
        else:
            block_loop_head = self.new_block()

        last_block.next_blocks.append(block_loop_head)

        # Build cfg from while body
        loop_body_block = self.block = self.new_block()
        block_loop_head.next_blocks.append(loop_body_block)
        block_loop_head.next_blocks.append(block_end_loop)

        self.build_on_block_or_stmt(node.body)

        # Add the back edge
        self.block.next_blocks.append(block_loop_head)

        # Handle probable break
        self.add_loop_control_edges(block_end_loop, block_loop_head)

        self.block = block_end_loop
        return False

    def build_on_do_while(self, node: nodes.DoWhileStmt) -> bool:
        # save the last block
        block_before_do_while = self.block

        # create the block after for loop structure
        block_end_loop = self.new_block()
        block_end_loop.tag_on_empty = "END_DO_WHILE"

        if node.predicate is not None:
            block_loop_predicate = self.new_block(node.predicate, kind="conditional")
        else:
            block_loop_predicate = self.new_block()

        block_do_while_body_start = self.block = self.new_block()
        block_before_do_while.next_blocks.append(block_do_while_body_start)
        self.build_on_block_or_stmt(node.body)

        self.block.next_blocks.append(block_loop_predicate)

        # Add next nodes for the loop predicate
        block_loop_predicate.next_blocks.append(block_do_while_body_start)
        block_loop_predicate.next_blocks.append(block_end_loop)

        # Handle probable break
        self.add_loop_control_edges(block_end_loop, block_do_while_body_start)

        self.block = block_end_loop
        return False

    def build_on_for(self, node: nodes.ForStmt) -> bool:
        # save the last block
        last_block = self.block

        # create the block after for loop structure
        block_end_for = self.new_block()
        block_end_for.tag_on_empty = "END_FOR"

        if node.init is not None:
            last_block.add_statement(node.init)

        if node.predicate is not None:
            block_loop_head = self.new_block(node.predicate, kind="conditional")
        else:
            block_loop_head = self.new_block()

        last_block.next_blocks.append(block_loop_head)

        loop_body_block = self.block = self.new_block()
        block_loop_head.next_blocks.append(loop_body_block)

        self.build_on_block_or_stmt(node.body)

        if node.update is not None:
            self.block.add_statement(node.update)

        # add back edge
        self.block.next_blocks.append(block_loop_head)

        # handle probable break
        self.add_loop_control_edges(block_end_for, block_loop_head)

        block_loop_head.next_blocks.append(block_end_for)
        self.block = block_end_for

        return False

    def build_on_return(self, node: nodes.ReturnStmt) -> bool:
        """
        Returns if the `build_on_block` method should return
        """
        # create the block after return
        next_block = self.new_block()
        next_block.add_statement(node)
        self.block.next_blocks.append(next_block)
        next_block.next_blocks.append(self.return_block)
        return True

    def build_on_goto(self, node: nodes.GoToStmt) -> bool:
        self.goto_edges.append((self.block, node.label))
        self.block.set_tag_on_empty(f"GOTO {node.label}")
        return True

    def build_on_break(self, node: nodes.BreakStmt) -> bool:
        self.loop_control_stmts.append(("break", self.block))
        self.block.set_tag_on_empty("BREAK")
        return True

    def build_on_continue(self, node: nodes.ContinueStmt) -> bool:
        self.loop_control_stmts.append(("continue", self.block))
        self.block.set_tag_on_empty("CONTINUE")
        return True


def expand_multi_stmt_nodes(cfg: "CFG"):
    """
    将CFG中有多个statement的节点进行展开
    注意：**此方法不是纯函数**，会对传入的CFG进行修改
    """
    multi_stmt_nodes: set[int] = set()
    for node in cfg.topology.nodes:
        if len(cfg.get_block(node).statements) > 1:
            multi_stmt_nodes.add(node)

    _id = max(cfg.topology.nodes)

    def new_id():
        nonlocal _id
        _id += 1
        return _id

    for node in multi_stmt_nodes:
        block_to_split = cfg.get_block(node)
        cfg._block_id_map.pop(block_to_split._id)

        # 获取前驱节点
        predecessors = list(cfg.topology.predecessors(node))

        # 将所有语句都存入单独的节点内
        # 然后形成一个链状结构
        all_created_blocks: list[BasicBlockData] = []  # 创建的全部节点
        for stmt in block_to_split.statements:
            # 创建新的语句节点
            new_block = BasicBlockData(new_id(), [stmt], "normal")

            # 如果存在前驱节点，就将链状结构的前驱节点连接到新节点
            if len(all_created_blocks) > 0:
                cfg.topology.add_edge(all_created_blocks[-1]._id, new_block._id)

            # 保存到列表内
            all_created_blocks.append(new_block)

            # 添加CFG中节点id到控制流节点数据的映射
            cfg._block_id_map[new_block._id] = new_block

        # 最后一个节点的kind应当与被分拆的节点一致
        all_created_blocks[-1].kind = block_to_split.kind

        # 获取block_to_split的所有后继节点
        # 并且创建从节点链最后一个节点，到所有后继节点的链接
        # 顺序应当与block_to_split的后继节点一致
        for next_block_to_connect in cfg.topology.neighbors(block_to_split._id):
            cfg.topology.add_edge(all_created_blocks[-1]._id, next_block_to_connect)

        # 用节点链的第一个节点
        # 替换到各个前驱节点指向block_to_split的边
        for pred_id in predecessors:
            graph_algorithms.update_out_edge_with_order(
                cfg.topology, pred_id, node, all_created_blocks[0]._id
            )
        # 最后移除被分割的节点，卸磨杀驴
        cfg.topology.remove_node(block_to_split._id)


def remove_empty_node_from_cfg(cfg: "CFG"):
    """
    zh:
    移除CFG中的空节点。由于CFG各个节点的出边是有顺序的，因此不能直接使用networkx中移除节点的方法
    注意：**此方法不是纯函数**，会对传入的CFG进行修改
    """
    # 获取所有空节点
    empty_nodes: set[int] = set()
    for node in cfg.topology.nodes:
        if len(cfg.get_block(node).statements) == 0 and not (
            cfg.entry_block.block_id == node or cfg.exit_block.block_id == node
        ):
            empty_nodes.add(node)

    # 对每一个空节点采取操作
    for node in empty_nodes:
        predecessors, successors = list(cfg.topology.predecessors(node)), list(
            cfg.topology.successors(node)
        )

        # 对于空节点的后继节点一定只有一个
        # 否则就存在问题
        assert len(successors) == 1

        # 获取后继节点
        successor_block_id = successors[0]

        # 获取要删除的节点
        block_to_remove = cfg.get_block(node)

        # 移除相应的节点
        cfg._block_id_map.pop(block_to_remove._id)

        # 将后继节点替换到各个前驱block的后继节点中
        for pred_id in predecessors:
            graph_algorithms.update_out_edge_with_order(
                cfg.topology, pred_id, node, successor_block_id
            )
        # 在拓扑结构中也移除相应的节点
        cfg.topology.remove_node(block_to_remove._id)
