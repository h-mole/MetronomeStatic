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


WL = []
PFG = nx.DiGraph()
pt: Dict[str, set] = {}
variables = {"a", "b", "c", "d", "e", "f", "c", "n1", "n2", "x", "y", "n", "C.m__this"}
RM = set()  # 可达的方法
CG = nx.DiGraph()
S = []
Sm = {
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
    "Number.get": []
}
parameters = {"C.main": [], "C.id": ["n"], "C.m": [], "Number.get": []}
ret_object_var = {"C.id": "n", "C.m": None, "Number.get": None}


def add_reachable(m_with_ctx: str):
    print("add_reachable", m_with_ctx)
    c, m = m_with_ctx.split(":")
    if m_with_ctx not in RM:
        RM.add(m_with_ctx)
        S.extend(Sm[m])
        inst_new: InstructionNew
        for inst_new in filter(lambda stmt: isinstance(stmt, InstructionNew), Sm[m]):
            WL.append((c + ":" + inst_new.variable, {f"{c}:" + inst_new.tag}))
        inst_assign: InstructionAssign
        for inst_assign in filter(
            lambda stmt: isinstance(stmt, InstructionAssign)
            and isinstance(stmt.r_value, str),
            Sm[m],
        ):
            add_edge(f"{c}:" + inst_assign.r_value, f"{c}:" + inst_assign.variable)


def add_edge(src: str, dst: str):
    if (src, dst) not in PFG.edges:
        PFG.add_edge(src, dst)
        pt_src_value = pt.get(src, set())
        if len(pt_src_value) != 0:
            WL.append((dst, pt_src_value))


def propagate(n, pts: Set[str]):
    if len(pts) > 0:
        if n not in pt:
            pt[n] = set()
        pt[n].update(pts)
        if n in PFG.nodes:
            for s in PFG.neighbors(n):
                WL.append((s, pts))


def dispatch(o_i, k):
    print("dispatch", o_i, k)
    key = {
        ("o_3", "m"): "C.m",
        ("o_3", "id"): "C.id",
        ("o_12", "get"): "Number.get",
    }[(o_i, k)]
    return key


def select(c, l, c__o_i):
    print("select", c, l, c__o_i)
    return l


def process_call(c_x: str, c__o_i):
    c, x = c_x.split(":")
    c_, o_i = c__o_i.split(":")
    print("\tprocess_call", c_x, c__o_i)
    call_instruction: InstructionCall
    for call_instruction in filter(
        lambda stmt: isinstance(stmt, InstructionCall)
        and stmt.name.variable == x,  # .split(".")[-1].split("__")[0],
        S,
    ):
        # print(call_instruction.__dict__)
        m = dispatch(o_i, call_instruction.name.field)
        print("dispatched_result", m)
        c_t = select(c, call_instruction.tag, c__o_i)
        c_prefix = f"{c}:"
        ct_prefix = f"{c_t}:"
        print("\tselected c and c_t", c, c_t)
        WL.append((c_t + ":" + m + "__this", {c_ + ":" + o_i}))
        if (c_prefix + call_instruction.tag, ct_prefix + m) not in CG:
            CG.add_edge(c_prefix + call_instruction.tag, ct_prefix + m)
            add_reachable(ct_prefix + m)
            for a_i, param in zip(call_instruction.args, parameters[m]):
                add_edge(c_prefix + a_i, ct_prefix + param)
            if ret_object_var[m] is not None:
                # print("tag", (ret_object_var[m] if ret_object_var[m] else call_instruction.tag))
                add_edge(
                    ct_prefix
                    + (
                        ret_object_var[m] if ret_object_var[m] else call_instruction.tag
                    ),
                    c_prefix + call_instruction.l_value,
                )


add_reachable(":C.main")
print(WL, PFG.edges)


def main():
    count = 0
    # sys.exit()
    while len(WL) > 0:
        n, pts = WL.pop(0)
        pt_n = pt.get(n, set())
        delta = pts - pt_n
        # print("delta", delta, "n", n)
        propagate(n, delta)
        # print(WL)
        # break
        print("n", n)
        print("delta", delta)
        c, _var_name = n.split(":")
        if _var_name in variables:
            for obj in delta:
                for store in filter(lambda s: isinstance(s, InstructionStore), S):
                    add_edge(f"{c}:" + store.value, obj + "." + store.field)
                for load in filter(lambda s: isinstance(s, InstructionLoad), S):
                    add_edge(obj + "." + load.field, load.target)
                process_call(n, obj)
        print("pt", pt)
        print("WL", WL)
        print("RM", RM)
        print("PFG EDGES", PFG.edges)
        print("CG EDGES", CG.edges)

        # print("pt_n", pt_n)
        print()
        if count > 1:
            pass
        count += 1

    print(PFG.edges)


main()
