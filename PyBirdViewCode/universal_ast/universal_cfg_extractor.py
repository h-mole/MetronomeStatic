import copy
from html import escape
from ..universal_ast import universal_ast_nodes as nodes
from typing import Dict, List, Literal, Tuple, Union, Optional
import networkx as nx
from .exceptions import OnBreakStatement
from ..algorithms import ValidNodeKinds

BlockKinds = Literal["normal", "conditional", "switch"]
LoopControlKinds = Literal["break", "continue"]


class BasicBlock:
    def __init__(
        self,
        id: int,
        statements: Optional[List[nodes.SourceElement]] = None,
        kind: BlockKinds = "normal",
    ):
        self._id = id
        self.statements = statements if statements is not None else []
        self.kind: BlockKinds = kind
        self.tag_on_empty = ""
        self.next_blocks: List[BasicBlock] = []

    @property
    def block_id(self):
        return self._id

    def add_statement(self, statement: nodes.SourceElement):
        self.statements.append(statement)

    def set_tag_on_empty(self, tag: str):
        self.tag_on_empty = tag

    def text_on_empty(self):
        return f"<Block>" if self.tag_on_empty == "" else f"<{self.tag_on_empty}>"

    def __repr__(self) -> str:
        return f"<BasicBlock #{self._id} {self.statements}>"


class CFG:
    """
    控制流图
    """

    def __init__(
        self, all_blocks: List[BasicBlock], entry_block_id: int, return_block_id: int
    ) -> None:
        self._all_blocks: List[BasicBlock] = all_blocks
        self._block_id_map: Dict[int, BasicBlock] = {
            block.block_id: block for block in self._all_blocks
        }
        self._entry_block = self._block_id_map[entry_block_id]
        self._return_block = self._block_id_map[return_block_id]
        self._topology = self._calc_topology()

    @property
    def topology(self) -> nx.DiGraph:
        """
        The topology of graph.
        """
        return self._topology

    def _calc_topology(self) -> nx.DiGraph:
        """
        Calculate the topology of the cfg.

        :return: a nx.DiGraph with same edges while nodes just contain theirs id.
        """
        g = nx.DiGraph()
        for block in self._all_blocks:
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

    def to_networkx(self):
        """
        Convert this CFG to a networkx graph
        """
        g = copy.deepcopy(self.topology)
        # get_edges(self.head_block)
        for block in self._all_blocks:
            label_base = f"#{block._id} {escape(block.text_on_empty())}\n"
            if len(block.statements) > 0:
                g.nodes[block._id]["label"] = label_base + "\n".join(
                    [str(stmt) for stmt in block.statements]
                )
            else:
                g.nodes[block._id]["label"] = label_base
        return g

    def print_graph(self):
        edges = []

        for block in self._all_blocks:
            edges.extend([(block._id, nb._id) for nb in block.next_blocks])
            print(block)
            print("\n")
        print(edges)

    def get_block(self, block_id: int):
        return self._block_id_map[block_id]


class CFGBuilder:
    def __init__(self) -> None:
        self._current_id = 0
        self.all_blocks: List[BasicBlock] = []
        self.block = self.new_block()
        self.head_block = self.block
        self.return_block = self.new_block()
        self.return_block.statements.append("METHOD_RETURN")

        # Goto edges are from "goto" node and to the label
        # The edges should add in the last step
        self.goto_edges: List[Tuple[BasicBlock, str]] = []
        # self.loop_control_edges: List[Tuple[BasicBlock, BasicBlock]] = []

        # Storing continue or Break statements to add
        self.loop_control_stmts: List[Tuple[LoopControlKinds, BasicBlock]] = []

    def search_block_with_label(self, label: str) -> BasicBlock:
        """
        Search through all basic blocks, and get the first block with a label
        """
        for block in self.all_blocks:
            if block._id == 13:
                print(block.statements)
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
                # print("added break! for ")
                print(
                    "added break! for ",
                    block_with_control_stmt._id,
                    block_with_control_stmt.next_blocks,
                )
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

    def build(self, ast: nodes.MethodDecl):
        assert isinstance(ast, nodes.MethodDecl)

        self.build_on_method_declaration(ast)
        return CFG(
            self.all_blocks, self.head_block.block_id, self.return_block.block_id
        )

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

        block_loop_predicate.next_blocks.append(block_end_loop)
        block_loop_predicate.next_blocks.append(block_do_while_body_start)

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
        print(self.loop_control_stmts)
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
