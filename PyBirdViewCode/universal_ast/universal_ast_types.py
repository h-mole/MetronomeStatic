from typing import List, Optional, Tuple, TYPE_CHECKING
from .universal_ast_nodes import SourceElement


class TypeElement(SourceElement):
    pass


class NotSpecificallyHandledType(TypeElement):
    _fields = ["name"]

    def __init__(self, name):
        self.name = name

class ParamType(TypeElement):
    _fields = ["name", "type"]

    def __init__(self, name: "Name", type: str):
        super(ParamType, self).__init__()
        self.name = name
        self.type = type

class CallableType(TypeElement):
    _fields = ["pos_args", "return_type", "modifiers"]

    def __init__(
        self,
        pos_args: List[ParamType],
        return_type: TypeElement,
        modifiers: Optional[List[str]] = None,
    ) -> None:
        self.pos_args = pos_args
        self.return_type = return_type
        self.modifiers = modifiers if modifiers is not None else []


all_type_names = {
    k
    for k, v in globals().items()
    if isinstance(v, type) and issubclass(v, TypeElement)
}
