"""
This file is copied from plyj package.
"""

from typing import (
    Any,
    Callable,
    Dict,
    Generator,
    List,
    Optional,
    Tuple,
    TypeVar,
    Union,
    Literal as LiteralType,
    TYPE_CHECKING,
    Type as TypingType,
)
import uuid
from itertools import chain
from MelodieFuncFlow import MelodieGenerator


if TYPE_CHECKING:
    from ..uast import universal_ast_types as types

DATA_TYPE = Union[
    "StructType",
    "ArrayType",
    "IntType",
    "VoidType",
    "FloatType",
    "UnknownType",
    "AddrReferenceType",
]

STANDARD_BINARY_OPERATORS: set[str] = {
    # Arithmetics
    "*",  # Times
    "+",  # Add
    "-",  # Subtract
    "/",  # Division
    "%",  # Mod
    "**",  # Power
    ",",  # Comma operator
    # Logics
    "&&",  # And
    "||",  # Or
    # Bitwise operators
    "|",  # Bitwise Or
    "^",  # Bitwise XOR
    "&",  # Bitwise and
    "<<",  # Left shift
    ">>",  # Right shift
    # Relationships
    "!=",  # Not equal
    "<=",  # Less than or equal
    "<",  # Less than
    "==",  # Equal
    ">=",  # Greater than or equal
    ">",  # Greater than
}

STANDARD_UNARY_OPERATORS: set[tuple[str, bool]] = {
    ("+", True),  # Plus (usage like "+a", "+1")
    ("-", True),  # Minus
    ("!", True),  # Not
    ("&", True),  # Address of
    ("*", True),  # Value of
    ("++", True),  # Pre-increment
    ("++", False),  # Post-increment
    ("--", True),  # Pre-decrement
    ("--", False),  # Post-decrement
    ("~", True),  # Bitwise not
}

STANDARD_ASSIGNMENTS: set[str] = {
    "=",
    "+=",
    "-=",
    "*=",
    "/=",
    "%=",
    "<<=",
    ">>=",
    "&=",
    "|=",
    "^=",
}


class SourceElement(object):
    """
    A SourceElement is the base class for all elements that occur in a Java
    file parsed by plyj.
    """

    class ApplyContext:
        def __init__(self) -> None:
            self.hierarchy: List[SourceElement] = []

        def print_hierarchy(self):
            print([c.__class__.__name__ for c in self.hierarchy])

        @property
        def current_node(self) -> "SourceElement":
            """
            Current node in the Clang AST
            """
            if len(self.hierarchy) > 0:
                return self.hierarchy[-1]
            else:
                raise ValueError("Traversal context does not contain any node.")

        def _push(self, node: "SourceElement"):
            self.hierarchy.append(node)

        def _pop(self):
            self.hierarchy.pop()

        def find_by_type(self, type: "TypingType[SourceElement]"):
            """
            Search the AST hierarchy, get the AST node of the same kind.
            """
            for item in self.hierarchy:
                if item.__class__ == type:
                    return item
            return None

        def find_by_type_td(self, type: "TypingType[SourceElement]"):
            """
            Perform top-down search by AST node kind in the hierarchy.
            """
            for item in reversed(self.hierarchy):
                if item.__class__ == type:
                    return item
            return None

        def nearest_block(self) -> Tuple["SourceElement", "SourceElement"]:
            """
            Find nearest Block Statement

            :return:
            """
            compound_stmt: Optional[BlockStmt] = None
            index = len(self.hierarchy)
            for item in reversed(self.hierarchy):
                index -= 1
                if item.__class__ in {BlockStmt}:
                    compound_stmt = item
                    break

            expr: SourceElement = self.hierarchy[index + 1]  # compound_stmt下的
            return compound_stmt, expr

        def __len__(self):
            return len(self.hierarchy)

    _common_fields: List[str] = ["id", "location"]
    _fields: List[str] = []

    def __init__(self):
        super(SourceElement, self).__init__()
        self.location: Tuple[Optional[int], Optional[int]] = (
            None,
            None,
        )  # line, column
        self.id = uuid.uuid4().hex

    def __repr__(self):
        # try:
        equals = (
            "{0}={1!r}".format(k, getattr(self, k))
            for k in chain(self._fields, self._common_fields)
        )
        args = ", ".join(equals)
        return "{0}({1})".format(self.__class__.__name__, args)

    def __eq__(self, other):
        try:
            return self.__dict__ == other.__dict__
        except AttributeError:
            return False

    def __ne__(self, other):
        return not self == other

    def accept(self, visitor):
        """
        default implementation that visit the subnodes in the order
        they are stored in self_field
        """
        class_name = self.__class__.__name__
        visit = getattr(visitor, "visit_" + class_name)
        if visit(self):
            for f in chain(self._fields, self._common_fields):
                field = getattr(self, f)
                if field:
                    if isinstance(field, list):
                        for elem in field:
                            if isinstance(elem, SourceElement):
                                elem.accept(visitor)
                    elif isinstance(field, SourceElement):
                        field.accept(visitor)
        getattr(visitor, "leave_" + class_name)(self)

    def _check_serializable(self, item, field_name):
        if not (isinstance(item, (int, float, str)) or item is None):
            raise ValueError(f"{item} {field_name}")

    @classmethod
    def from_dict(cls, dic: Dict[str, Any]):
        """
        Load this element from the json-serializable dict
        """
        if "_cls" not in dic:
            raise KeyError("Invalid dictionary without key `_cls`")
        cls_name: str = dic["_cls"]
        node_cls = globals()[cls_name]
        params_dict = {}
        for k, v in dic.items():
            if k == "_cls":
                continue
            else:
                if isinstance(v, dict) and "_cls" in v:
                    params_dict[k] = cls.from_dict(v)
                elif isinstance(v, list):
                    new_list = []
                    for elem in v:
                        if isinstance(elem, dict) and "_cls" in elem:
                            new_list.append(cls.from_dict(elem))
                        else:
                            new_list.append(elem)
                    params_dict[k] = new_list
                else:
                    params_dict[k] = v

        return node_cls(**params_dict)

    @classmethod
    def _single_item_to_serializable(
        cls, item: Any
    ) -> Union[None, int, str, float, bool, tuple, List, Dict]:
        if isinstance(item, SourceElement):
            new_dict: Dict[str, Any] = {"_cls": item.__class__.__name__}
            for field_name in chain(item._fields, item._common_fields):
                field_value = getattr(item, field_name)
                new_dict[field_name] = cls._single_item_to_serializable(field_value)
            return new_dict
        elif isinstance(item, list):
            return [cls._single_item_to_serializable(list_item) for list_item in item]
        else:
            assert isinstance(item, (int, str, float, bool, tuple)) or item is None, (
                item,
                type(item),
            )
            return item

    def to_dict(self):
        """
        Convert this element to a json-serializable dict
        """
        return self._single_item_to_serializable(self)

    def _apply_func_to_uast(
        self, walk_func: Callable[[ApplyContext], bool], ctx: ApplyContext
    ):
        ctx._push(self)

        ret = walk_func(ctx)
        if ret:
            for f in chain(self._fields, self._common_fields):
                field = getattr(self, f)
                if field:
                    if isinstance(field, list):
                        for elem in field:
                            if isinstance(elem, SourceElement):
                                elem._apply_func_to_uast(walk_func, ctx)
                    elif isinstance(field, SourceElement):
                        field._apply_func_to_uast(walk_func, ctx)
        ctx._pop()

    def apply_with_hierarchy(self, walk_func: Callable[[ApplyContext], bool]):
        """
        Walk through the UAST applying the `walk_func` to each node
        """
        ctx = self.ApplyContext()
        self._apply_func_to_uast(walk_func, ctx)

    def walk_preorder(self) -> Generator["SourceElement", None, None]:
        for f in chain(self._fields, self._common_fields):
            field = getattr(self, f)
            if field:
                if isinstance(field, list):
                    for elem in field:
                        if isinstance(elem, SourceElement):
                            yield from elem.walk_preorder()
                elif isinstance(field, SourceElement):
                    yield from field.walk_preorder()
        yield self

    def iter_nodes(self) -> MelodieGenerator["SourceElement"]:
        return MelodieGenerator(self.walk_preorder())

    def filter_by(
        self, _type: Optional[Union[TypingType["T"], Tuple]] = None, **props
    ) -> MelodieGenerator["T"]:
        def filter_func(node: SourceElement) -> bool:
            if _type is not None and not isinstance(node, _type):
                return False
            for k, v in props.items():
                if getattr(node, k) != props[k]:
                    return False
            return True

        return self.iter_nodes().filter(filter_func)


T = TypeVar("T", bound=SourceElement)


class CompilationUnit(SourceElement):
    _fields = ["children"]

    def __init__(
        self,
        children: List[SourceElement],
    ):
        super(CompilationUnit, self).__init__()
        self.children = children


class PackageDecl(SourceElement):
    _fields = ["name", "modifiers"]

    def __init__(self, name, modifiers=None):
        super(PackageDecl, self).__init__()

        if modifiers is None:
            modifiers = []
        self.name = name
        self.modifiers = modifiers


class ImportDecl(SourceElement):
    _fields = ["name", "static", "on_demand", "path"]

    def __init__(self, name, path="", static=False, on_demand=False):
        super(ImportDecl, self).__init__()
        self.name = name
        self.static = static
        self.on_demand = on_demand
        self.path = path


class StructDecl(SourceElement):
    _fields = [
        "name",
        "fields",
    ]

    def __init__(self, name, fields: List["FieldDecl"]):
        super().__init__()
        self.name = name
        self.fields = fields


class UnionDecl(SourceElement):
    _fields = [
        "name",
        "children",
    ]

    def __init__(self, name, children: List["FieldDecl"]):
        super().__init__()
        self.name = name
        self.children = children


class ClassDecl(SourceElement):
    _fields = [
        "name",
        "body",
        "modifiers",
        "type_parameters",
        "extends",
        "implements",
    ]

    def __init__(
        self,
        name,
        body,
        modifiers=None,
        type_parameters=None,
        extends=None,
        implements=None,
    ):
        super(ClassDecl, self).__init__()

        if modifiers is None:
            modifiers = []
        if type_parameters is None:
            type_parameters = []
        if implements is None:
            implements = []
        self.name = name
        self.body = body
        self.modifiers = modifiers
        self.type_parameters = type_parameters
        self.extends = extends
        self.implements = implements


class ClassInitializer(SourceElement):
    _fields = ["block", "static"]

    def __init__(self, block, static=False):
        super(ClassInitializer, self).__init__()
        self.block = block
        self.static = static


class ConstructorDecl(SourceElement):
    _fields = [
        "name",
        "block",
        "modifiers",
        "type_parameters",
        "parameters",
        "throws",
    ]

    def __init__(
        self,
        name,
        block,
        modifiers=None,
        type_parameters=None,
        parameters=None,
        throws=None,
    ):
        super(ConstructorDecl, self).__init__()
        if modifiers is None:
            modifiers = []
        if type_parameters is None:
            type_parameters = []
        if parameters is None:
            parameters = []
        self.name = name
        self.block = block
        self.modifiers = modifiers
        self.type_parameters = type_parameters
        self.parameters = parameters
        self.throws = throws


class EmptyDecl(SourceElement):
    pass


class FieldDecl(SourceElement):
    _fields = ["name", "type", "modifiers"]

    def __init__(self, name: str, type: DATA_TYPE, init_value=None, modifiers=None):
        super(FieldDecl, self).__init__()
        if modifiers is None:
            modifiers = []
        self.name = name
        self.type = type
        self.init_value = init_value
        # self.variable_declarators = variable_declarators
        self.modifiers = modifiers


class MethodType(SourceElement):
    _fields = ["pos_args", "return_type", "modifiers"]

    def __init__(
        self,
        pos_args: List["ParamDecl"],
        return_type: List[SourceElement],
        modifiers: Optional[List[str]] = None,
    ) -> None:
        super().__init__()
        self.pos_args = pos_args
        self.return_type = return_type
        self.modifiers = modifiers if modifiers is not None else []


class VoidType(SourceElement):
    _fields = []

    def __init__(self):
        super().__init__()


class IntType(SourceElement):
    _fields = ["bits", "signed"]

    def __init__(self, bits: int = 0, signed=True):
        """
        :bits: Memory bits storing this integer.
        :signed: Whether this integer is signed or unsigned
        """
        super().__init__()
        assert bits >= 0
        self.bits = bits
        self.signed = signed


class FloatType(SourceElement):
    _fields = ["bits"]

    def __init__(self, bits: int = 64):
        super().__init__()
        self.bits = bits


class UserDefinedType(SourceElement):
    _fields = ["name"]

    def __init__(self, name: str):
        super().__init__()
        self.name = name


class AddrReferenceType(SourceElement):
    _fields = ["referee"]

    def __init__(self, referee: DATA_TYPE):
        super().__init__()
        self.referee = referee


class ArrayType(SourceElement):
    _fields = ["elem_type", "length"]

    def __init__(self, elem_type: DATA_TYPE, length: Optional[SourceElement] = None):
        super().__init__()
        self.elem_type = elem_type
        self.length = length


class UnknownType(SourceElement):
    _fields = ["type"]

    def __init__(self, type_str: str):
        super().__init__()
        self.type: str = type_str


class MethodDecl(SourceElement):
    """
    en:

    Declaration of a method or function.
    If `body` is not None, this node is also a definition.

    zh:

    函数或方法的声明。如果``body``为``None``，那么这个节点也是函数的定义

    """

    _fields = [
        "name",  # Name of method
        # "modifiers",
        "type",  # Return type of method
        # "type_parameters",
        # "parameters",
        # "return_type",
        "body",
        "abstract",
        "extended_dims",
        "throws",
        "type_ref",
    ]

    def __init__(
        self,
        name: Optional["Name"],
        type: MethodType,
        # modifiers=None,
        # type_parameters=None,
        # parameters=None,
        # return_type="void",
        body: Optional["BlockStmt"] = None,
        abstract=False,
        extended_dims=0,
        throws=None,
        type_ref=None,
    ):
        super(MethodDecl, self).__init__()
        # if modifiers is None:
        #     modifiers = []
        # if type_parameters is None:
        #     type_parameters = []
        # if parameters is None:
        #     parameters = []
        # if type_ref is Non
        self.name = name
        self.type = type
        # self.modifiers = modifiers
        # self.type_parameters = type_parameters
        # self.parameters = parameters
        # self.return_type = return_type
        self.body = body
        self.abstract = abstract
        self.extended_dims = extended_dims
        self.throws = throws
        self.type_ref = type_ref


class FormalParameter(SourceElement):
    _fields = ["variable", "type", "modifiers", "vararg"]

    def __init__(self, variable, type, modifiers=None, vararg=False):
        super(FormalParameter, self).__init__()
        if modifiers is None:
            modifiers = []
        self.variable = variable
        self.type = type
        self.modifiers = modifiers
        self.vararg = vararg


class Variable(SourceElement):
    # I would like to remove this class. In theory, the dimension could be added
    # to the type but this means variable declarations have to be changed
    # somehow. Consider 'int i, j[];'. In this case there currently is only one
    # type with two variable declarators;This closely resembles the source code.
    # If the variable is to go away, the type has to be duplicated for every
    # variable...
    _fields = ["name", "dimensions"]

    def __init__(self, name, dimensions=0):
        super(Variable, self).__init__()
        self.name = name
        self.dimensions = dimensions


class VarDecl(SourceElement):
    _fields = ["variable", "initializer", "type"]

    def __init__(self, variable: "Name", initializer=None, type=None):
        super(VarDecl, self).__init__()
        self.variable = variable
        self.initializer = initializer
        self.type = type


class CompoundDecl(SourceElement):
    """
    zh:

    定义多个变量的语句
    """

    _fields = ["decls"]

    def __init__(self, decls: List[VarDecl]):
        super().__init__()
        self.decls = decls


class ParamDecl(SourceElement):
    _fields = ["name", "type"]

    def __init__(self, name: "Name", type: DATA_TYPE):
        super(ParamDecl, self).__init__()
        assert isinstance(name, Name)
        self.name = name
        self.type = type


class Throws(SourceElement):
    _fields = ["types"]

    def __init__(self, types):
        super(Throws, self).__init__()
        self.types = types


class InterfaceDecl(SourceElement):
    _fields = ["name", "modifiers", "extends", "type_parameters", "body"]

    def __init__(
        self, name, modifiers=None, extends=None, type_parameters=None, body=None
    ):
        super(InterfaceDecl, self).__init__()
        if modifiers is None:
            modifiers = []
        if extends is None:
            extends = []
        if type_parameters is None:
            type_parameters = []
        if body is None:
            body = []
        self.name = name
        self.modifiers = modifiers
        self.extends = extends
        self.type_parameters = type_parameters
        self.body = body


class EnumDecl(SourceElement):
    _fields = ["name", "implements", "modifiers", "type_parameters", "body"]

    def __init__(
        self,
        name,
        implements: List["EnumConst"],
        modifiers=None,
        type_parameters=None,
        body=None,
    ):
        super(EnumDecl, self).__init__()
        if implements is None:
            implements = []
        if modifiers is None:
            modifiers = []
        if type_parameters is None:
            type_parameters = []
        if body is None:
            body = []
        self.name = name
        self.implements = implements
        self.modifiers = modifiers
        self.type_parameters = type_parameters
        self.body = body


class EnumConst(SourceElement):
    """
    An item out of a declaration of variable
    """

    _fields = ["name", "value"]

    def __init__(self, name, value=None):
        super(EnumConst, self).__init__()
        self.name = name
        self.value = value


class AnnotationDecl(SourceElement):
    _fields = [
        "name",
        "modifiers",
        "type_parameters",
        "extends",
        "implements",
        "body",
    ]

    def __init__(
        self,
        name,
        modifiers=None,
        type_parameters=None,
        extends=None,
        implements=None,
        body=None,
    ):
        super(AnnotationDecl, self).__init__()
        if modifiers is None:
            modifiers = []
        if type_parameters is None:
            type_parameters = []
        if implements is None:
            implements = []
        if body is None:
            body = []
        self.name = name
        self.modifiers = modifiers
        self.type_parameters = type_parameters
        self.extends = extends
        self.implements = implements
        self.body = body


class AnnotationMethodDecl(SourceElement):
    _fields = [
        "name",
        "type",
        "parameters",
        "default",
        "modifiers",
        "type_parameters",
        "extended_dims",
    ]

    def __init__(
        self,
        name,
        type,
        parameters=None,
        default=None,
        modifiers=None,
        type_parameters=None,
        extended_dims=0,
    ):
        super(AnnotationMethodDecl, self).__init__()
        if parameters is None:
            parameters = []
        if modifiers is None:
            modifiers = []
        if type_parameters is None:
            type_parameters = []
        self.name = name
        self.type = type
        self.parameters = parameters
        self.default = default
        self.modifiers = modifiers
        self.type_parameters = type_parameters
        self.extended_dims = extended_dims


class Annotation(SourceElement):
    _fields = ["name", "members", "single_member"]

    def __init__(self, name, members=None, single_member=None):
        super(Annotation, self).__init__()
        if members is None:
            members = []
        self.name = name
        self.members = members
        self.single_member = single_member


class AnnotationMember(SourceElement):
    _fields = ["name", "value"]

    def __init__(self, name, value):
        super(SourceElement, self).__init__()
        self.name = name
        self.value = value


class Type(SourceElement):
    """
    For typedef statements
    """

    _fields = ["name", "type_arguments", "enclosed_in", "dimensions"]

    def __init__(self, name, type_arguments=None, enclosed_in=None, dimensions=0):
        super(Type, self).__init__()
        if type_arguments is None:
            type_arguments = []
        self.name = name
        self.type_arguments = type_arguments
        self.enclosed_in = enclosed_in
        self.dimensions = dimensions


class Wildcard(SourceElement):
    _fields = ["bounds"]

    def __init__(self, bounds=None):
        super(Wildcard, self).__init__()
        if bounds is None:
            bounds = []
        self.bounds = bounds


class WildcardBound(SourceElement):
    _fields = ["type", "extends", "_super"]

    def __init__(self, type, extends=False, _super=False):
        super(WildcardBound, self).__init__()

        self.type = type
        self.extends = extends
        self._super = _super


class TypeParam(SourceElement):
    _fields = ["name", "extends"]

    def __init__(self, name, extends=None):
        super(TypeParam, self).__init__()
        if extends is None:
            extends = []
        self.name = name
        self.extends = extends


class Expr(SourceElement):
    def __init__(self):
        super(Expr, self).__init__()


class ExprStmt(SourceElement):
    _fields = ["expr"]

    def __init__(self, expr: SourceElement):
        super().__init__()
        self.expr = expr


class BinaryExpr(Expr):
    _fields = ["operator", "lhs", "rhs"]

    def __init__(self, operator: str, lhs: SourceElement, rhs: SourceElement):
        super(BinaryExpr, self).__init__()
        self.operator = operator
        self.lhs = lhs
        self.rhs = rhs
        if self.__class__ == BinaryExpr:
            assert operator in STANDARD_BINARY_OPERATORS, operator


class Assignment(Expr):
    _fields = ["operator", "lhs", "rhs"]
    operator: str
    lhs: List[SourceElement]
    rhs: List[SourceElement]

    def __init__(
        self, operator: str, lhs: List[SourceElement], rhs: List[SourceElement]
    ):
        super().__init__()
        self.operator = operator
        self.lhs = lhs
        self.rhs = rhs

        assert isinstance(self.lhs, list)
        assert isinstance(self.rhs, list)
        if self.__class__ == Assignment:
            assert operator in STANDARD_ASSIGNMENTS, operator


class Conditional(Expr):
    _fields = ["predicate", "if_true", "if_false"]

    def __init__(self, predicate, if_true, if_false):
        super(Conditional, self).__init__()
        self.predicate = predicate
        self.if_true = if_true
        self.if_false = if_false


class UnaryExpr(Expr):
    _fields = ["sign", "expression", "op_before_expr"]

    def __init__(self, sign, expression, op_before_expr: bool):
        super(UnaryExpr, self).__init__()
        self.sign = sign
        self.expression = expression
        # self.op_pos = op_pos
        self.op_before_expr = op_before_expr
        if self.__class__ == UnaryExpr:
            assert (self.sign, self.op_before_expr) in STANDARD_UNARY_OPERATORS, (
                self.sign,
                self.op_before_expr,
            )


class CastExpr(Expr):
    _fields = ["target_type", "expr_type", "expression", "style"]

    def __init__(
        self,
        target_type: "DATA_TYPE",
        expr_type: "DATA_TYPE",
        expression,
        style: LiteralType["c", "cxx_static"],
    ):
        super(CastExpr, self).__init__()
        self.target_type = target_type
        self.style = style
        self.expr_type = expr_type
        self.expression = expression


class Stmt(SourceElement):
    pass


class EmptyStmt(Stmt):
    pass


class BlockStmt(Stmt):
    _fields = ["statements"]

    def __init__(self, statements=None):
        super(Stmt, self).__init__()
        if statements is None:
            statements = []
        self.statements = statements

    def __iter__(self):
        for s in self.statements:
            yield s


# class VarDecl(Stmt, FieldDecl):
#     pass


class ArrayInitializer(SourceElement):
    _fields = ["elements"]

    def __init__(self, elements: Optional[List[SourceElement]] = None):
        super(ArrayInitializer, self).__init__()
        if elements is None:
            elements = []
        self.elements = elements


class StructInitializer(SourceElement):
    """
    Initializer containing field name and theirs value.
    like Node{[]string{"a", "b"}}

    :fields: can be any expr. especially a k-v pair
    """

    _fields: List[SourceElement] = ["type", "fields"]

    def __init__(
        self,
        type: SourceElement,
        fields: List[SourceElement],
    ):
        super().__init__()
        self.type = type
        self.fields = fields
        # self.named_fields = named_fields


class CallExpr(Expr):
    _fields = ["name", "arguments", "type_arguments", "target"]

    def __init__(self, name, arguments=None, type_arguments=None, target=None):
        super(CallExpr, self).__init__()
        if arguments is None:
            arguments = []
        if type_arguments is None:
            type_arguments = []
        self.name = name
        self.arguments = arguments
        self.type_arguments = type_arguments
        self.target = target


class IfThenElseStmt(Stmt):
    _fields = ["predicate", "if_true", "if_false"]

    def __init__(self, predicate, if_true, if_false=None):
        super(IfThenElseStmt, self).__init__()
        self.predicate = predicate
        self.if_true = if_true
        self.if_false = if_false


class WhileStmt(Stmt):
    _fields = ["predicate", "body"]

    def __init__(self, predicate, body: BlockStmt):
        super(WhileStmt, self).__init__()
        self.predicate = predicate
        self.body = body


class ForStmt(Stmt):
    _fields = ["init", "predicate", "update", "body"]

    def __init__(self, init, predicate, update, body):
        super(ForStmt, self).__init__()
        self.init = init
        self.predicate = predicate
        self.update = update
        self.body = body


class ForEachStmt(Stmt):
    _fields = ["type", "variable", "iterable", "body", "modifiers"]

    def __init__(self, type, variable, iterable, body, modifiers=None):
        super(ForEachStmt, self).__init__()
        if modifiers is None:
            modifiers = []
        self.type = type
        self.variable = variable
        self.iterable = iterable
        self.body = body
        self.modifiers = modifiers


class AssertStmt(Stmt):
    _fields = ["predicate", "message"]

    def __init__(self, predicate, message=None):
        super(AssertStmt, self).__init__()
        self.predicate = predicate
        self.message = message


class SwitchStmt(Stmt):
    _fields = ["expression", "switch_cases"]

    def __init__(self, expression, switch_cases: List["SwitchCase"]):
        super(SwitchStmt, self).__init__()
        self.expression = expression
        self.switch_cases = switch_cases

    def get_default_case(self) -> Optional["SwitchCase"]:
        for case in self.switch_cases:
            if isinstance(case.case, DefaultStmt):
                return case
        return None


class DefaultStmt(SourceElement):
    def __init__(self):
        super().__init__()


class SwitchCase(SourceElement):
    _fields = ["case", "body"]

    def __init__(
        self,
        case: List[Union[SourceElement, DefaultStmt]],
        body: Union[BlockStmt, SourceElement],
    ):
        super(SwitchCase, self).__init__()
        self.case = case
        assert isinstance(self.case, list), self.case
        self.body = body


class DoWhileStmt(Stmt):
    _fields = ["predicate", "body"]

    def __init__(self, predicate, body: BlockStmt = None):
        super(DoWhileStmt, self).__init__()
        self.predicate = predicate
        self.body = body


class ContinueStmt(Stmt):
    _fields = ["label"]

    def __init__(self, label=None):
        super(ContinueStmt, self).__init__()
        self.label = label


class BreakStmt(Stmt):
    _fields = ["label"]

    def __init__(self, label=None):
        super(BreakStmt, self).__init__()
        self.label = label


class ReturnStmt(Stmt):
    _fields = ["result"]

    def __init__(self, result: Optional[List[SourceElement]] = None):
        super(ReturnStmt, self).__init__()
        if result is None:
            result = []
        self.result: List[SourceElement] = result
        assert isinstance(self.result, list)


class SynchronizedStmt(Stmt):
    _fields = ["monitor", "body"]

    def __init__(self, monitor, body):
        super(SynchronizedStmt, self).__init__()
        self.monitor = monitor
        self.body = body


class ThrowStmt(Stmt):
    _fields = ["exception"]

    def __init__(self, exception):
        super(ThrowStmt, self).__init__()
        self.exception = exception


class TryStmt(Stmt):
    _fields = ["block", "catches", "_finally", "resources"]

    def __init__(self, block, catches=None, _finally=None, resources=None):
        super(TryStmt, self).__init__()
        if catches is None:
            catches = []
        if resources is None:
            resources = []
        self.block = block
        self.catches = catches
        self._finally = _finally
        self.resources = resources

    def accept(self, visitor):
        if visitor.visit_Try(self):
            for s in self.block:
                s.accept(visitor)
        for c in self.catches:
            visitor.visit_Catch(c)
        if self._finally:
            self._finally.accept(visitor)


class CatchStmt(SourceElement):
    _fields = ["variable", "modifiers", "types", "block"]

    def __init__(self, variable, modifiers=None, types=None, block=None):
        super(CatchStmt, self).__init__()
        if modifiers is None:
            modifiers = []
        if types is None:
            types = []
        self.variable = variable
        self.modifiers = modifiers
        self.types = types
        self.block = block


class Resource(SourceElement):
    _fields = ["variable", "type", "modifiers", "initializer"]

    def __init__(self, variable, type=None, modifiers=None, initializer=None):
        super(Resource, self).__init__()
        if modifiers is None:
            modifiers = []
        self.variable = variable
        self.type = type
        self.modifiers = modifiers
        self.initializer = initializer


class ConstructorCallStmt(Stmt):
    """An explicit invocations of a class's constructor.

    This is a variant of either this() or super(), NOT a "new" expression.
    """

    _fields = ["name", "target", "type_arguments", "arguments"]

    def __init__(self, name, target=None, type_arguments=None, arguments=None):
        super(ConstructorCallStmt, self).__init__()
        if type_arguments is None:
            type_arguments = []
        if arguments is None:
            arguments = []
        self.name = name
        self.target = target
        self.type_arguments = type_arguments
        self.arguments = arguments


class InstanceCreationExpr(Expr):
    _fields = ["type", "type_arguments", "arguments", "body", "enclosed_in"]

    def __init__(
        self, type, type_arguments=None, arguments=None, body=None, enclosed_in=None
    ):
        super(InstanceCreationExpr, self).__init__()

        if type_arguments is None:
            type_arguments = []
        if arguments is None:
            arguments = []
        if body is None:
            body = []
        self.type = type
        self.type_arguments = type_arguments
        self.arguments = arguments
        self.body = body
        self.enclosed_in = enclosed_in


class FieldAccessExpr(Expr):
    """
    属性的访问语句，比如``a.b``
    如果target是None，代表访问所在的类的属性
    """

    _fields = ["name", "target"]

    def __init__(self, name: str, target: Optional[SourceElement]):
        super(FieldAccessExpr, self).__init__()

        self.name = name
        self.target = target


class ArrayAccessExpr(Expr):
    """
    zh:

    数组的访问语句，比如``a[0]``
    """

    _fields = ["index", "target"]

    def __init__(self, index, target):
        super(ArrayAccessExpr, self).__init__()
        self.index = index
        self.target = target


class ArrayCreation(Expr):
    _fields = ["type", "dimensions", "initializer"]

    def __init__(self, type, dimensions=None, initializer=None):
        super(ArrayCreation, self).__init__()
        if dimensions is None:
            dimensions = []
        self.type = type
        self.dimensions = dimensions
        self.initializer = initializer


class Literal(SourceElement):
    _fields = ["value", "kind"]

    def __init__(self, value, kind: str):
        super(Literal, self).__init__()
        self.value = value
        self.kind = kind


class ClassLiteral(SourceElement):
    _fields = ["type"]

    def __init__(self, type):
        super(ClassLiteral, self).__init__()
        self.type = type


class Name(SourceElement):
    _fields = ["id"]

    def __init__(self, name: str):
        super(Name, self).__init__()
        self.id = name


# class ExpressionStatement(Stmt):
#     _fields = ["expression"]

#     def __init__(self, expression):
#         super(ExpressionStatement, self).__init__()
#         self.expression = expression


class ReferenceExpr(Expr):
    """
    zh:

    取地址操作，类似于``&p``
    """

    _fields = ["value"]

    def __init__(self, value):
        super(ReferenceExpr, self).__init__()
        self.value = value


class DereferenceExpr(Expr):
    """
    zh:

    指针的取值操作，类似于``*p``
    """

    _fields = ["ref"]

    def __init__(self, ref):
        super(DereferenceExpr, self).__init__()
        self.ref = ref


class KeyValuePair(SourceElement):
    """

    K-V 键值对表达式
    """

    _fields = ["key", "value"]

    def __init__(self, key: SourceElement, value: SourceElement):
        super().__init__()
        self.key = key
        self.value = value


class SpecialExpr(SourceElement):
    """
    en:

    Operator that are not evaluated like normal Unary/Binary Operator.
    For example: `sizeof` operator in C

    zh:

    特殊操作符，与普通的Unary/Binary Operator不同，例如C中的`sizeof`操作符
    """

    _fields = [
        "name",
        "arguments",
    ]

    def __init__(self, name: str, arguments: List[str]):
        super().__init__()
        self.name = name
        self.arguments = arguments


class Label(SourceElement):
    _fields = ["name", "statement"]

    def __init__(self, name: str, stmt: Optional[SourceElement] = None):
        super(Label, self).__init__()
        self.name = name
        self.statement = stmt


class AddressLabel(SourceElement):
    _fields = ["name"]

    def __init__(self, name: str):
        super().__init__()
        self.name = name


class GoToStmt(SourceElement):
    _fields = ["label", "direct"]
    """
    If direct, label is a str. Or the label is a SourceElement
    """

    def __init__(self, label: Union[str, SourceElement], direct: bool = True):
        super(GoToStmt, self).__init__()
        self.label = label
        self.direct = direct


class Using(SourceElement):
    _fields = ["used"]

    def __init__(self, used: Union["NameSpaceRef", SourceElement]):
        super().__init__()
        self.used = used


class AccessSpecfier(SourceElement):
    _fields = ["kind"]

    def __init__(self, kind):
        super().__init__()
        self.kind = kind


class Yield(SourceElement):
    """
    Yield is used in Python or C#
    """

    _fields = ["value"]

    def __init__(self, value):
        super().__init__()
        self.value = value


class YieldFrom(SourceElement):
    _fields = ["target"]

    def __init__(self, target):
        super().__init__()
        self.target = target


class NameSpaceDef(SourceElement):
    """
    Define a namespace
    """

    _fields = ["name", "children"]

    def __init__(self, name, children: List[SourceElement]):
        super().__init__()
        self.name = name
        self.children = children


class NameSpaceRef(SourceElement):
    """
    Refer to a namespace
    """

    _fields = ["name"]

    def __init__(self, name: str):
        super().__init__()
        self.name = name


class Visitor(object):

    def __init__(self, verbose=False):
        self.verbose = verbose

    def __getattr__(self, name):
        from ..uast import universal_ast_types as types

        if not (name.startswith("visit_") or name.startswith("leave_")):
            raise AttributeError(
                "name must start with visit_ or leave_ but was {}".format(name)
            )
        else:
            cls = name.split("_")[1]
            assert (cls in globals()) or (cls in types.all_type_names), name

        def f(element):
            if self.verbose:
                msg = "unimplemented call to {}; ignoring ({})"
                print(msg.format(name, element))
            return True

        return f


class NotImplementedItem(SourceElement):
    _fields = ["kind"]

    def __init__(self, kind: str) -> None:
        super().__init__()
        self.kind = kind

    # def __repr__(self) -> str:
    #     return f"<NotimplementedItem {self.kind}>"


# TO update this "__ALL__":
# ", ".join(["\""+k+'"' for k, v in uast.__dict__.items()
#               if type(v) == type and issubclass(v, uast.SourceElement)])
__ALL__ = [
    "SourceElement",
    "CompilationUnit",
    "PackageDecl",
    "ImportDecl",
    "StructDecl",
    "UnionDecl",
    "ClassDecl",
    "ClassInitializer",
    "ConstructorDecl",
    "EmptyDecl",
    "FieldDecl",
    "MethodType",
    "IntType",
    "VoidType",
    "FloatType",
    "ArrayType",
    "UnknownType",
    "MethodDecl",
    "FormalParameter",
    "Variable",
    "VarDecl",
    "CompoundDecl",
    "ParamDecl",
    "Throws",
    "InterfaceDecl",
    "EnumDecl",
    "EnumConst",
    "AnnotationDecl",
    "AnnotationMethodDecl",
    "Annotation",
    "AnnotationMember",
    "Type",
    "Wildcard",
    "WildcardBound",
    "TypeParam",
    "Expr",
    "ExprStmt",
    "BinaryExpr",
    "Assignment",
    "Conditional",
    "UnaryExpr",
    "CastExpr",
    "Stmt",
    "EmptyStmt",
    "BlockStmt",
    "ArrayInitializer",
    "StructInitializer",
    "CallExpr",
    "IfThenElseStmt",
    "WhileStmt",
    "ForStmt",
    "ForEachStmt",
    "AssertStmt",
    "SwitchStmt",
    "DefaultStmt",
    "SwitchCase",
    "DoWhileStmt",
    "ContinueStmt",
    "BreakStmt",
    "ReturnStmt",
    "SynchronizedStmt",
    "ThrowStmt",
    "TryStmt",
    "CatchStmt",
    "Resource",
    "ConstructorCallStmt",
    "InstanceCreationExpr",
    "FieldAccessExpr",
    "ArrayAccessExpr",
    "ArrayCreation",
    "Literal",
    "ClassLiteral",
    "Name",
    "ReferenceExpr",
    "DereferenceExpr",
    "KeyValuePair",
    "SpecialExpr",
    "Label",
    "AddressLabel",
    "GoToStmt",
    "Using",
    "AccessSpecfier",
    "Yield",
    "YieldFrom",
    "NameSpaceDef",
    "NameSpaceRef",
    "NotImplementedItem",
]
