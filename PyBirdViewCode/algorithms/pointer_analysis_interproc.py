from typing import Dict, Set
import networkx as nx


class PAInstruction:
    def __init__(self) -> None:
        self.tag = ""


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


A_main_statements = [
    InstructionNew("a", "A", "o_3"),
    InstructionNew("b", "B", "o_4"),
    InstructionCall(InstructionLoad("b", "foo"), ["a"], "c", "L5"),
]
A_foo_statements = []

B_foo_statements = [InstructionNew("r", "A", "o_11"), InstructionReturn("r")]


WL = []
PFG = nx.DiGraph()
pt: Dict[str, set] = {}
variables = {"a", "b", "c", "d", "e", "f"}
RM = set()
CG = nx.DiGraph()
S = []
Sm = {"A.main": A_main_statements, "A.foo": A_foo_statements, "B.foo": B_foo_statements}
parameters = {"A.foo": ["x"], "B.foo": ["y"]}
ret_object_var = {"B.foo": "r"}


def add_reachable(m: str):
    if m not in RM:
        RM.add(m)
        S.extend(Sm[m])
        inst_new: InstructionNew
        for inst_new in filter(lambda stmt: isinstance(stmt, InstructionNew), Sm[m]):
            WL.append((inst_new.variable, {inst_new.tag}))
        inst_assign: InstructionAssign
        for inst_assign in filter(
            lambda stmt: isinstance(stmt, InstructionAssign)
            and isinstance(stmt.r_value, str),
            Sm[m],
        ):
            add_edge(inst_assign.r_value, inst_assign.variable)


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
    # raise NotImplementedError
    stmts = Sm["B.foo"]
    return "B.foo"


def process_call(x, o_i):
    print("process_call", x, o_i)
    call_instruction: InstructionCall
    for call_instruction in filter(
        lambda stmt: isinstance(stmt, InstructionCall) and stmt.name.variable == x, S
    ):
        print(call_instruction.__dict__)
        m = dispatch(call_instruction.name.variable, call_instruction.name.field)

        WL.append((m + "_this", {o_i}))
        if (call_instruction.tag, m) not in CG:
            CG.add_edge(call_instruction.tag, m)
            add_reachable(m)
            for a_i, param in zip(call_instruction.args, parameters[m]):
                add_edge(a_i, param)
            add_edge(ret_object_var[m], call_instruction.l_value)


add_reachable("A.main")
print(WL, PFG.edges)
count = 0
while len(WL) > 0:
    n, pts = WL.pop(0)
    delta = pts - pt.get(n, set())
    # print("delta", delta, "n", n)
    propagate(n, delta)
    # print(WL)
    # break
    if n in variables:
        for obj in delta:
            for store in filter(lambda s: isinstance(s, InstructionStore), S):
                add_edge(store.value, obj + "." + store.field)
            for load in filter(lambda s: isinstance(s, InstructionLoad), S):
                add_edge(obj + "." + load.field, load.target)
            process_call(n, obj)
    print("WL", WL)
    print("EDGES", PFG.edges)
    print()
    if count > 1:
        pass
    count += 1

print(PFG.edges)
