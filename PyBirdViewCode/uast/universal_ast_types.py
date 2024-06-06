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


all_type_names = {
    k
    for k, v in globals().items()
    if isinstance(v, type) and issubclass(v, TypeElement)
}
