"""
Storing information about the program
"""

import collections
from typing import Dict, Optional

from clang.cindex import Cursor

from ..utils import MelodieFrozenGenerator
from ..clang_utils.code_attributes import (
    DefModel,
    FieldDefModel,
    FunctionDefModel,
    StructDefModel,
)
from .models import StructValue, Variable


class ProgramInfo:
    def __init__(
        self,
        functions: Dict[str, Cursor],
        structures: Optional[MelodieFrozenGenerator[DefModel]] = None,
    ) -> None:
        self.functions = functions
        self.structures = structures if structures else MelodieFrozenGenerator([])

    def get_function_structure(self, name: str) -> FunctionDefModel:
        structure = self.structures.filter(lambda x: x.spelling == name).head()
        return structure

    def get_function_ast(self, name: str) -> Cursor:
        """
        Get function AST by name
        """
        return self.functions[name]

    # def get_variable_type(self, name: str) -> Optional[ConcreteValueType]:
    #     """
    #     Get type by variable name
    #     """
    #     return self.structures.filter(lambda x: x.spelling == name).head().type

    def allocate_memory(self, type_name: str) -> Variable:
        """
        Allocate struct by name
        """
        # For standard types
        if type_name in ("int", "unsigned int", "float", "double"):
            return Variable(None)
        # For Non-standard Types
        else:
            try:
                stru_def: StructDefModel = self.structures.filter(
                    lambda x: isinstance(x, (StructDefModel,))
                    and x.spelling == type_name
                ).head()
            except StopIteration:
                raise Exception(f"Cannot handle type '{type_name}'")
            fields: collections.OrderedDict[str, Variable] = collections.OrderedDict()
            for field in stru_def.fields:
                if isinstance(field, FieldDefModel):
                    fields[field.spelling] = self.allocate_memory(field.type.spelling)
            return Variable(StructValue(fields))
            # elif isinstance(field.type, ArrayType):
            #     self.allocate_memory(field.type.element_type.spelling)
