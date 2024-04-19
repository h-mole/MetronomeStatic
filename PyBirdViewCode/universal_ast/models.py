"""
Models for AST
"""

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, List, Literal, OrderedDict, Tuple, Union

from clang.cindex import CursorKind
from dataclasses_json import DataClassJsonMixin
import warnings


if TYPE_CHECKING:
    CursorKind: Any = CursorKind
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

DATA_TYPE = Union[
    "StructType", "ArrayType", Literal["integer", "char", "float", "string"]
]


@dataclass
class StructType:
    attr_types: List[Tuple[str, DATA_TYPE]]


@dataclass
class ArrayType:
    element_type: DATA_TYPE
