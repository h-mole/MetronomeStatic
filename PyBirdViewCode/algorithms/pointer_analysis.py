from typing import Dict, Set
import networkx as nx


class PAInstruction:
    pass


class InstructionNew(PAInstruction):
    def __init__(self, variable: str, cls: str):
        self.variable = variable
        self.cls = cls


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
    def __init__(self, variable: str, field: str, target):
        self.variable = variable
        self.field = field
        self.target = target


statements = [
    InstructionNew("b", "C"),
    InstructionAssign("a", "b"),
    InstructionNew("c", "C"),
    InstructionStore("c", "f", "a"),
    InstructionAssign("d", "c"),
    InstructionStore("c", "f", "d"),
    InstructionLoad("d", "f", "e"),
]

WL = []
PFG = nx.DiGraph()
pt: Dict[str, set] = {}
variables = {"a", "b", "c", "d", "e", "f"}


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
        for s in PFG.neighbors(n):
            WL.append((s, pts))


new_objs_count = 1
for s in statements:
    if isinstance(s, InstructionNew):
        WL.append((s.variable, {f"o_{new_objs_count}"}))
        new_objs_count += 2
    if isinstance(s, InstructionAssign):
        add_edge(s.r_value, s.variable)
print(WL, PFG.edges)
while len(WL) > 0:
    n, pts = WL.pop(0)
    delta = pts - pt.get(n, set())
    print("delta", delta, "n", n)
    propagate(n, delta)
    print(WL)
    if n in variables:
        for obj in delta:
            for store in filter(lambda s: isinstance(s, InstructionStore), statements):
                add_edge(store.value, obj + "." + store.field)
            for load in filter(lambda s: isinstance(s, InstructionLoad), statements):
                add_edge(obj + "." + load.field, load.target)
    print(WL)
print(PFG.edges)