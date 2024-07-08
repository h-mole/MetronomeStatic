import sys

from PyBirdViewCode.uast.uast_commands import extract_cfg_from_method
from PyBirdViewCode.uast.universal_code_property_graphs import (
    get_cdg_topology,
    add_label,
)

sys.path.append("../../")
import networkx as nx

# from PyBirdViewCode
from PyBirdViewCode import (
    FileManager,
    get_file_uast,
    get_method_cpg,
    get_pdg_from_cfg,
    build_control_dependence_graph,
    # add_label,
    UASTQuery,
    uast,
    BaseUASTUnparser,
)

# 在当前路径下创建FileManager对象
fm = FileManager(".")


class Analyzer:
    def __init__(self) -> None:
        # 获取文件的UAST
        self.file_uast = get_file_uast("demo.c")
        self.unparser = BaseUASTUnparser()

    def create_output_nodes(self, call_expr: uast.CallExpr):
        pre_process_vertices = []
        post_process_vertices = []

        init_vertices = []
        final_vertices = []

        funcdef_uast = UASTQuery.get_method(
            self.file_uast, self.unparser.unparse(call_expr.name)
        )

        # 解析参数输入节点
        for formal_param, actual_param in zip(
            funcdef_uast.type.pos_args, call_expr.arguments
        ):
            # print(formal_param)
            match formal_param:
                case uast.ParamDecl(type=uast.AddrReferenceType(), name=arg_name):
                    print(formal_param.type, arg_name)
                    pre_process_vertices.append(
                        uast.Assignment(
                            "=",
                            lhs=[
                                uast.DereferenceExpr(
                                    uast.Name(
                                        f"$delta<{self.unparser.unparse(call_expr.name)}>({self.unparser.unparse(arg_name)})"
                                    )
                                )
                            ],
                            rhs=[uast.DereferenceExpr(actual_param)],
                        )
                    )
                    post_process_vertices.append(
                        uast.Assignment(
                            "=",
                            lhs=[uast.DereferenceExpr(actual_param)],
                            rhs=[
                                uast.DereferenceExpr(
                                    uast.Name(
                                        f"$delta'<{self.unparser.unparse(call_expr.name)}>({self.unparser.unparse(arg_name)})"
                                    )
                                )
                            ],
                        )
                    )
                    init_vertices.append(
                        uast.Assignment(
                            "=",
                            lhs=[uast.DereferenceExpr(arg_name)],
                            rhs=[
                                uast.DereferenceExpr(
                                    uast.Name(
                                        f"$delta<{self.unparser.unparse(call_expr.name)}>({self.unparser.unparse(arg_name)})"
                                    )
                                )
                            ],
                        )
                    )
                    final_vertices.append(
                        uast.Assignment(
                            "=",
                            lhs=[
                                uast.DereferenceExpr(
                                    uast.Name(
                                        f"$delta'<{self.unparser.unparse(call_expr.name)}>({self.unparser.unparse(arg_name)})"
                                    )
                                )
                            ],
                            rhs=[uast.DereferenceExpr(arg_name)],
                        )
                    )
                case uast.ParamDecl(name=arg_name):
                    pre_process_vertices.append(
                        uast.Assignment(
                            "=",
                            lhs=[
                                uast.Name(
                                    f"$delta<{self.unparser.unparse(call_expr.name)}>({self.unparser.unparse(arg_name)})"
                                )
                            ],
                            rhs=[actual_param],
                        )
                    )

        print("=======pre proc=======")
        for pre_prep in pre_process_vertices:
            print(self.unparser.unparse(pre_prep))
        print("=======post proc======")

        for pre_prep in post_process_vertices:
            print(self.unparser.unparse(pre_prep))
        print("=======init======")
        for pre_prep in init_vertices:
            print(self.unparser.unparse(pre_prep))
        print("=======final======")
        for pre_prep in final_vertices:
            print(self.unparser.unparse(pre_prep))
        return pre_process_vertices, post_process_vertices

    def analyse_function(self, func_name: str):
        # 通过UASTQuery，获取函数的UAST
        func_uast = UASTQuery.get_method(self.file_uast, func_name)

        # 抽取代码属性图
        cpgs = get_method_cpg(func_uast)

        pdg_main: nx.DiGraph = cpgs.pdg_nx.reverse(False)
        # fm.dot_dump(pdg_main, "p/"cdg_main.dot", export_png=True)

        for node_id in pdg_main.nodes:
            stmts = cpgs._cfg.get_block(node_id).statements
            if len(stmts) == 0:
                continue

            if len(exprs := (stmts[0].filter_by(uast.CallExpr).l)) > 0:
                assert len(exprs) == 1
                call_expr = exprs[0]
                print(pdg_main.nodes[node_id])

                preprocess, postprocess = self.create_output_nodes(call_expr)

                cfg = extract_cfg_from_method(func_uast, remove_empty_nodes=False)
                fm.dot_dump(cfg.to_networkx(), "cfg_main.dot", export_png=True)
                add_controlled_stmt_nodes(cfg, node_id, preprocess + postprocess)
                # cfg.topology.remove_edge(10, 4)
                # cfg.topology.add_edge(10, 10)

                # CDG的算法只适用于有向无环图？

                cdg_nx = build_control_dependence_graph(cfg.topology)
                add_label(cfg.to_networkx(), cdg_nx)
                fm.dot_dump(
                    cfg.to_networkx(), "cfg_main_processed.dot", export_png=True
                )
                # ddg_nx = ddg
                fm.dot_dump(cdg_nx, "cdg_main_processed.dot", export_png=True)

                new_pdg = get_pdg_from_cfg(cfg, [], [])
                fm.dot_dump(new_pdg, "pdg_main_processed.dot", export_png=True)
                break
        #  = self.create_delta_nodes(func_uast)


def add_controlled_stmt_nodes(
    cfg: uast.CFG, control_node_id: int, statements: list[uast.SourceElement]
) -> None:
    # 控制节点的后继节点
    control_node_successors = list(cfg.topology.successors(control_node_id))
    assert len(control_node_successors) == 1

    # 相当于可以增加一个从控制节点，经过statements形成的节点链，指向后继节点的分支，而原连边保持不动。
    # 这样会使得控制流图与代码的实际逻辑不符，但可以增加控制依赖

    added_blocks: list[uast.BasicBlockData] = []
    for stmt in statements:
        stmt_block = uast.BasicBlockData(cfg.new_node_id(), [stmt], "normal")
        cfg.add_block(stmt_block)
        if len(added_blocks) > 0:
            cfg.add_edge(added_blocks[-1].block_id, stmt_block.block_id)
        added_blocks.append(stmt_block)

    cfg.topology.add_edge(control_node_id, added_blocks[0].block_id)
    cfg.topology.add_edge(added_blocks[-1].block_id, control_node_successors[0])
    # cfg.topology.add_edge(added_blocks[-1].block_id, control_node_id)


analyzer = Analyzer()
analyzer.analyse_function("main")
# analyzer.analyse_function("A")
# analyzer.analyse_function("Increment")
# analyzer.analyse_function("Add")

# cpg_A = get_method_cpg(A_uast)
# pdg_A = cpg_A.pdg_nx.reverse(True)
# fm.dot_dump(pdg_A, "pdg_A.dot", export_png=True)
