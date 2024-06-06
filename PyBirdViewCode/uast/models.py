"""
Models for AST
"""

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, List, Literal, OrderedDict, Tuple, Union

from dataclasses_json import DataClassJsonMixin

# from .universal_ast_nodes import SourceElement


if TYPE_CHECKING:
    from z3 import ArithRef


@dataclass
class VarRef(DataClassJsonMixin):
    type: Literal["global", "local"]
    identifier: str


@dataclass
class Variable:
    value: "ConcreteValueType"


@dataclass
class StructValue:
    attributes: OrderedDict[str, Variable]
    # type: Optional["StructType"] = None


@dataclass
class ArrayValue:
    values: List[Variable]


@dataclass
class PointerValue:
    pointee: Variable


ConcreteValueType = Union[
    StructValue, ArrayValue, PointerValue, None, str, int, float, bool, "ArithRef"
]


# @dataclass
# class StructType:
#     attr_types: List[Tuple[str, DATA_TYPE]]


# @dataclass
# class ArrayType:
#     element_type: DATA_TYPE
