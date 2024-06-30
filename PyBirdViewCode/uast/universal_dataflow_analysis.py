from typing import List

import networkx as nx

from .universal_cfg_extractor import CFG
from .unparser import BaseUASTUnparser
from ..uast import universal_ast_nodes as nodes
from ..algorithms import RDAOp, RDAOpList, reaching_definition_analysis


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
            case nodes.CallExpr(arguments=arguments):
                for arg in arguments:
                    self.r_values.update(self.parse_value(arg))
            case nodes.AssertStmt():
                ret = self.parse_value(stmt.predicate)
                self.r_values.update(ret)
            case _:
                raise NotImplementedError(stmt)


def rda_on_cfg(cfg: CFG, arg_variables: List[str]):
    """
    在CFG对象上进行可达定义分析
    注意，传入的CFG需要保证每个节点上只有一个语句
    """
    unparser = BaseUASTUnparser()
    defs: dict[str, RDAOpList] = {}
    var_refs: dict[str, List[str]] = {}

    for node in cfg.topology.nodes:
        block = cfg.get_block(node)
        defs[node] = RDAOpList([])
        var_refs[node] = []
        if node == 1:
            defs[node].ops.extend([RDAOp(var_name) for var_name in arg_variables])
        if len(block.statements) == 0:
            pass
        elif len(block.statements) == 1:
            stmt = block.statements[0]
            assigned_variable = None
            parser = ReferencedRValueParser()
            parser.parse_referenced_values(stmt)
            match stmt:
                case nodes.Assignment(lhs=[lhs_item]):
                    assigned_variable = (
                        0,
                        unparser.unparse(lhs_item),
                        lhs_item.location,
                    )

                case nodes.UnaryExpr(sign="++" | "--"):
                    assigned_variable = (
                        0,
                        unparser.unparse(stmt.expression),
                        stmt.location,
                    )
                case _:
                    pass
            print("referenced_values", parser.r_values)
            if assigned_variable is not None:
                print(node, assigned_variable)
                stmt_index_, assigned_var_name_, loc = assigned_variable
                op = RDAOp(
                    assigned_var_name_,
                    used_var=list(parser.r_values),
                    location=loc,
                )
                # )
                defs[node].ops.append(op)
            var_refs[node] = list(parser.r_values)
            # defs[node].ops[0].used_var = list(parser.r_values)
        else:
            raise ValueError
    # import pdb; pdb.set_trace()
    # print(defs)
    _, _2, var_defs_reachable = reaching_definition_analysis(
        cfg.topology,
        {
            k: v
            for k, v in defs.items()
            if len(v.ops) == 0 or v.ops[0].defined_var != ""
        },
        [],
    )
    # for k, v in var_defs_reachable.items():
    #     print(k)
    #     print(v)
    #     print(var_refs[k])

    # print(var_defs_reachable)
    return var_defs_reachable, var_refs
