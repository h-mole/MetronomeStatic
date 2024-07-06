# 参考：https://blog.csdn.net/qq_46485137/article/details/131683056
from typing import Dict, Set
import networkx as nx


class PAInstruction:
    def __init__(self) -> None:
        self.tag = ""

    def __repr__(self) -> str:
        return str(self.__dict__)


class InstructionNew(PAInstruction):
    def __init__(self, variable: str, cls: str, tag: str):
        # super().__init__()
        self.variable = variable
        self.cls = cls
        self.tag = tag


class InstructionAssign(PAInstruction):
    def __init__(self, variable: str, r_value):
        self.variable = variable
        self.r_value = r_value


class InstructionStore(PAInstruction):
    def __init__(self, variable: str, field: str, value):
        self.variable = variable
        self.field = field
        self.value = value


class InstructionLoad(PAInstruction):
    def __init__(self, variable: str, field: str, target=None):
        self.variable = variable
        self.field = field
        self.target = target


class InstructionCall(PAInstruction):
    def __init__(self, name: "InstructionLoad", args, l_value, tag: str) -> None:
        # super().__init__()
        self.name = name
        self.args = args
        self.l_value = l_value
        self.tag = tag


class InstructionReturn(PAInstruction):
    def __init__(self, value) -> None:
        # super().__init__()
        self.value = value


class ContextSensitivePointerAnalysis:
    def __init__(self) -> None:
        self.WL = []
        self.PFG = nx.DiGraph()
        self.pt: Dict[str, set] = {}
        self.variables = {
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
            "c",
            "n1",
            "n2",
            "x",
            "y",
            "n",
            "C.m__this",
        }
        self.RM = set()  # 可达的方法
        self.CG = nx.DiGraph()
        self.S = []
        self.Sm = {
            "C.main": [
                InstructionNew("c", "C", "o_3"),
                InstructionCall(InstructionLoad("c", "m"), [], None, "L4"),
            ],
            "C.m": [
                InstructionNew("n1", "One", "o_12"),
                InstructionNew("n2", "Two", "o_13"),
                InstructionCall(InstructionLoad("C.m__this", "id"), ["n1"], "x", "L14"),
                InstructionCall(InstructionLoad("C.m__this", "id"), ["n2"], "y", "L15"),
                InstructionCall(InstructionLoad("x", "get"), [], None, "L16"),
            ],
            "C.id": [],
            "Number.get": [],
        }
        self.parameters = {"C.main": [], "C.id": ["n"], "C.m": [], "Number.get": []}
        self.ret_object_var = {"C.id": "n", "C.m": None, "Number.get": None}
        self.dispatch_keys = {
            ("o_3", "m"): "C.m",
            ("o_3", "id"): "C.id",
            ("o_12", "get"): "Number.get",
            ("o_13", "get"): "Number.get",
        }

        self.add_reachable(":C.main")
        print(self.WL, self.PFG.edges)

    def add_reachable(self, m_with_ctx: str):
        print("add_reachable", m_with_ctx)
        c, m = m_with_ctx.split(":")
        if m_with_ctx not in self.RM:
            self.RM.add(m_with_ctx)
            self.S.extend(self.Sm[m])
            inst_new: InstructionNew
            for inst_new in filter(
                lambda stmt: isinstance(stmt, InstructionNew), self.Sm[m]
            ):
                self.WL.append((c + ":" + inst_new.variable, {f"{c}:" + inst_new.tag}))
            inst_assign: InstructionAssign
            for inst_assign in filter(
                lambda stmt: isinstance(stmt, InstructionAssign)
                and isinstance(stmt.r_value, str),
                self.Sm[m],
            ):
                self.add_edge(
                    f"{c}:" + inst_assign.r_value, f"{c}:" + inst_assign.variable
                )

    def add_edge(self, src: str, dst: str):
        if (src, dst) not in self.PFG.edges:
            self.PFG.add_edge(src, dst)
            pt_src_value = self.pt.get(src, set())
            if len(pt_src_value) != 0:
                self.WL.append((dst, pt_src_value))

    def propagate(self, n, pts: Set[str]):
        if len(pts) > 0:
            if n not in self.pt:
                self.pt[n] = set()
            self.pt[n].update(pts)
            if n in self.PFG.nodes:
                for s in self.PFG.neighbors(n):
                    self.WL.append((s, pts))

    def dispatch(self, o_i, k) -> str:

        key = self.dispatch_keys[(o_i, k)]
        return key

    def select(self, ctx, label, c__o_i, m):
        """
        通过传入的一系列参数，求目标方法的上下文

        :ctx: 语句所在方法的上下文
        :label: 调用点，语句的label标签
        :c__o_i: 接收到的对象
        :m: 目标方法
        """

        raise NotImplementedError

    def process_call(self, c_x: str, c__o_i):
        c, x = c_x.split(":")
        c_, o_i = c__o_i.split(":")
        print("\tprocess_call", c_x, c__o_i)
        call_instruction: InstructionCall
        for call_instruction in filter(
            lambda stmt: isinstance(stmt, InstructionCall)
            and stmt.name.variable == x,  # .split(".")[-1].split("__")[0],
            self.S,
        ):
            # print(call_instruction.__dict__)
            m = self.dispatch(o_i, call_instruction.name.field)
            print("dispatched_result", m)
            c_t = self.select(c, call_instruction.tag, c__o_i, m)
            c_prefix = f"{c}:"
            ct_prefix = f"{c_t}:"
            print("\tselected c and c_t", c, c_t)
            self.WL.append((c_t + ":" + m + "__this", {c_ + ":" + o_i}))
            if (c_prefix + call_instruction.tag, ct_prefix + m) not in self.CG:
                self.CG.add_edge(c_prefix + call_instruction.tag, ct_prefix + m)
                self.add_reachable(ct_prefix + m)
                for a_i, param in zip(call_instruction.args, self.parameters[m]):
                    self.add_edge(c_prefix + a_i, ct_prefix + param)
                if self.ret_object_var[m] is not None:
                    # print("tag", (ret_object_var[m] if ret_object_var[m] else call_instruction.tag))
                    self.add_edge(
                        ct_prefix
                        + (
                            self.ret_object_var[m]
                            if self.ret_object_var[m]
                            else call_instruction.tag
                        ),
                        c_prefix + call_instruction.l_value,
                    )

    def main(self):
        count = 0
        # sys.exit()
        while len(self.WL) > 0:
            n, pts = self.WL.pop(0)
            pt_n = self.pt.get(n, set())
            delta = pts - pt_n
            # print("delta", delta, "n", n)
            self.propagate(n, delta)
            # print(WL)
            # break
            print("n", n)
            print("delta", delta)
            c, _var_name = n.split(":")
            if _var_name in self.variables:
                for obj in delta:
                    for store in filter(
                        lambda s: isinstance(s, InstructionStore), self.S
                    ):
                        self.add_edge(f"{c}:" + store.value, obj + "." + store.field)
                    for load in filter(
                        lambda s: isinstance(s, InstructionLoad), self.S
                    ):
                        self.add_edge(obj + "." + load.field, load.target)
                    self.process_call(n, obj)
            print("pt", self.pt)
            print("WL", self.WL)
            print("RM", self.RM)
            print("PFG EDGES", self.PFG.edges)
            print("CG EDGES", self.CG.edges)

            # print("pt_n", pt_n)
            print()
            if count > 1:
                pass
            count += 1

        print(self.PFG.edges)


class CallSiteSensitivePointerAnalysis(ContextSensitivePointerAnalysis):
    def select(self, ctx, label, c__o_i, m):
        return label


class ObjectSensitivePointerAnalysis(ContextSensitivePointerAnalysis):
    def select(self, ctx, label, c__o_i: str, m):
        return c__o_i.split(":")[1]


# CallSiteSensitivePointerAnalysis().main()
