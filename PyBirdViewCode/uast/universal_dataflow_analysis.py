from typing import List, Optional

import networkx as nx

from .universal_cfg_extractor import CFG, BasicBlockData
from .unparser import BaseUASTUnparser
from ..uast import universal_ast_nodes as nodes
from ..algorithms import (
    RDAOp,
    RDAOpList,
    reaching_definition_analysis,
    graph_algorithms,
)

INTER_PROCEDURAL = True


class ReferencedRValueParser:
    def __init__(self) -> None:
        self.r_values: set[str] = set()

    def parse_single(self, stmt: nodes.SourceElement) -> str:
        match stmt:
            case nodes.FieldAccessExpr(name=name, target=target):
                target_str = self.parse_single(target)
                return f"{target_str}.{name}"
            case nodes.Name():
                return stmt.id
            case nodes.Literal():
                return repr(stmt.value)
            case nodes.ArrayAccessExpr(index=index, target=target):
                target_str = self.parse_single(target)
                index_str = self.parse_single(index)
                return f"{target_str}[{index_str}]"
            case _:
                raise NotImplementedError(stmt)

    def parse_value(self, stmt: nodes.SourceElement) -> set[str]:
        match stmt:
            case nodes.Null():
                return set()
            case nodes.FieldAccessExpr() | nodes.Name():
                return {self.parse_single(stmt)}
            case nodes.Literal():
                return set()
            case nodes.BinaryExpr(lhs=lhs, rhs=rhs):
                return self.parse_value(lhs) | self.parse_value(rhs)
            case nodes.CallExpr(name=name, arguments=arguments):
                if not INTER_PROCEDURAL:
                    parsed = set()
                    for arg in arguments:
                        parsed |= self.parse_value(arg)
                    match name:
                        # 如果被调用的是对象的方法，那么相应的对象当然也是依赖的
                        case nodes.FieldAccessExpr(target=target):
                            parsed.update(self.parse_value(target))
                        case _:
                            pass
                    return parsed
                else:
                    return set()
            case nodes.AssertStmt():
                return self.parse_value(stmt.predicate)
            case nodes.ArrayAccessExpr(index=index, target=target):
                return self.parse_value(index) | self.parse_value(target)
            case nodes.UnaryExpr(expression=expr):
                return self.parse_value(expr)
            # case nodes.CompoundDecl()
            case _:
                raise NotImplementedError(stmt)

    def parse_referenced_values(self, stmt: nodes.SourceElement):
        match stmt:
            case nodes.Assignment(rhs=rhs):
                for item in rhs:
                    self.parse_referenced_values(item)
            case nodes.BinaryExpr(lhs=lhs, rhs=rhs):
                self.parse_referenced_values(lhs)
                self.parse_referenced_values(rhs)
            case nodes.UnaryExpr(expression=expr):
                self.parse_referenced_values(expr)
            case nodes.Literal() | nodes.Null():
                return None
            case nodes.Name():
                self.r_values.add(stmt.id)
            case nodes.FieldAccessExpr():
                self.r_values.update(self.parse_value(stmt))
            case nodes.AssertStmt() | nodes.CallExpr():
                ret = self.parse_value(stmt)
                self.r_values.update(ret)
            case nodes.ReturnStmt():
                if stmt.result is not None:
                    for ret in stmt.result:
                        self.parse_referenced_values(ret)
            case nodes.VarDecl(variable=variable, initializer=initializer):
                if initializer is not None:
                    self.parse_referenced_values(initializer)
            case nodes.CompoundDecl(decls=decls):
                for decl in decls:
                    self.parse_referenced_values(decl)
            case nodes.DereferenceExpr():
                self.parse_referenced_values(stmt.ref)
            case nodes.ReferenceExpr():
                self.parse_referenced_values(stmt.value)
            case _:
                raise NotImplementedError(stmt)


def match_lvalue(
    unparser: BaseUASTUnparser, stmt: nodes.SourceElement
) -> List[tuple[str, nodes.LocationType]]:
    match stmt:
        case nodes.Assignment(lhs=[lhs_item]):
            return [
                (
                    unparser.unparse(lhs_item),
                    lhs_item.location,
                )
            ]

        case nodes.UnaryExpr(sign="++" | "--"):
            return [
                (
                    unparser.unparse(stmt.expression),
                    stmt.location,
                )
            ]
        case nodes.CompoundDecl():
            values = []
            for var_decl in stmt.decls:
                values.extend(match_lvalue(unparser, var_decl))
            return values
        case nodes.VarDecl():
            return [(unparser.unparse(stmt.variable), stmt.location)]
        case _:
            return []


def rda_on_cfg(cfg: CFG, arg_variables: List[str]):
    """
    在CFG对象上进行可达定义分析
    注意:

    1. 传入的CFG需要保证每个节点上只有一个语句
    """
    unparser = BaseUASTUnparser()
    defs: dict[int, RDAOpList] = {}
    var_refs: dict[str, List[str]] = {}

    # 为CFG添加一个进入块ENTRY，block_id为-1。
    # 进入块中定义函数的各个参数
    NODE = "ENTRY"
    if NODE not in cfg.topology.nodes:
        cfg.add_edge(NODE, cfg.entry_block.block_id)
        cfg.add_block(BasicBlockData(NODE, statements=[]))
    for node in cfg.topology.nodes:
        block = cfg.get_block(node)
        if node != NODE:
            defs[node] = RDAOpList([])
            var_refs[node] = []
        else:
            defs[NODE] = RDAOpList([RDAOp(var_name) for var_name in arg_variables])
            var_refs[NODE] = []

        if len(block.statements) == 0:
            pass
        elif len(block.statements) == 1:
            stmt = block.statements[0]
            parser = ReferencedRValueParser()
            parser.parse_referenced_values(stmt)

            for assigned_variable in match_lvalue(unparser, stmt):
                assigned_var_name_, loc = assigned_variable
                op = RDAOp(
                    assigned_var_name_,
                    used_var=list(parser.r_values),
                    location=loc,
                )
                defs[node].ops.append(op)
            var_refs[node] = list(parser.r_values)
        else:
            raise ValueError

    _, _2, var_defs_reachable = reaching_definition_analysis(
        cfg.topology,
        {
            k: v
            for k, v in defs.items()
            if len(v.ops) == 0 or v.ops[0].defined_var != ""
        },
        [],
    )
    return var_defs_reachable, var_refs
