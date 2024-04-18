"""
This file is copied from plyj package.
"""

from typing import Any, Dict, Generator, List, Optional, Union


class SourceElement(object):
    """
    A SourceElement is the base class for all elements that occur in a Java
    file parsed by plyj.
    """

    _fields: List[str] = []

    def __init__(self):
        super(SourceElement, self).__init__()

    def __repr__(self):
        equals = ("{0}={1!r}".format(k, getattr(self, k)) for k in self._fields)
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
            for f in self._fields:
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
                params_dict[k] = (
                    cls.from_dict(v) if isinstance(v, dict) and "_cls" in v else v
                )
        return node_cls(**params_dict)

    def to_dict(self):
        """
        Convert this element to a json-serializable dict
        """
        new_dict: Dict[str, Any] = {"_cls": self.__class__.__name__}

        for field_name in self._fields:
            field_value = getattr(self, field_name)
            if isinstance(field_value, list):
                new_list = []
                for elem in field_value:
                    if isinstance(elem, SourceElement):
                        new_list.append(elem.to_dict())
                    else:
                        # self.check_serializable(elem, field_name)
                        new_list.append(elem)
                new_dict[field_name] = new_list
            else:
                if isinstance(field_value, SourceElement):
                    new_dict[field_name] = field_value.to_dict()
                else:
                    # self.check_serializable(field_value, field_name)
                    new_dict[field_name] = field_value
        return new_dict

    def walk_preorder(self) -> Generator["SourceElement", None, None]:
        for f in self._fields:
            field = getattr(self, f)
            if field:
                if isinstance(field, list):
                    for elem in field:
                        if isinstance(elem, SourceElement):
                            yield from elem.walk_preorder()
                elif isinstance(field, SourceElement):
                    yield from field.walk_preorder()


class CompilationUnit(SourceElement):
    _fields = ["children"]

    def __init__(
        self,
        children: List[SourceElement],
    ):
        super(CompilationUnit, self).__init__()
        self.children = children


class PackageDeclaration(SourceElement):
    _fields = ["name", "modifiers"]

    def __init__(self, name, modifiers=None):
        super(PackageDeclaration, self).__init__()

        if modifiers is None:
            modifiers = []
        self.name = name
        self.modifiers = modifiers


class ImportDeclaration(SourceElement):
    _fields = ["name", "static", "on_demand"]

    def __init__(self, name, static=False, on_demand=False):
        super(ImportDeclaration, self).__init__()
        self.name = name
        self.static = static
        self.on_demand = on_demand


class ClassDeclaration(SourceElement):
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
        super(ClassDeclaration, self).__init__()

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


class ConstructorDeclaration(SourceElement):
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
        super(ConstructorDeclaration, self).__init__()
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


class EmptyDeclaration(SourceElement):
    pass


class FieldDeclaration(SourceElement):
    _fields = ["type", "variable_declarators", "modifiers"]

    def __init__(self, type, variable_declarators, modifiers=None):
        super(FieldDeclaration, self).__init__()
        if modifiers is None:
            modifiers = []
        self.type = type
        self.variable_declarators = variable_declarators
        self.modifiers = modifiers


class MethodDeclaration(SourceElement):
    _fields = [
        "name",
        "modifiers",
        "type_parameters",
        "parameters",
        "return_type",
        "body",
        "abstract",
        "extended_dims",
        "throws",
    ]

    def __init__(
        self,
        name,
        modifiers=None,
        type_parameters=None,
        parameters=None,
        return_type="void",
        body: Optional["Block"] = None,
        abstract=False,
        extended_dims=0,
        throws=None,
    ):
        super(MethodDeclaration, self).__init__()
        if modifiers is None:
            modifiers = []
        if type_parameters is None:
            type_parameters = []
        if parameters is None:
            parameters = []
        self.name = name
        self.modifiers = modifiers
        self.type_parameters = type_parameters
        self.parameters = parameters
        self.return_type = return_type
        self.body = body
        self.abstract = abstract
        self.extended_dims = extended_dims
        self.throws = throws


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


class VariableDeclarator(SourceElement):
    _fields = ["variable", "initializer"]

    def __init__(self, variable, initializer=None):
        super(VariableDeclarator, self).__init__()
        self.variable = variable
        self.initializer = initializer


class Throws(SourceElement):
    _fields = ["types"]

    def __init__(self, types):
        super(Throws, self).__init__()
        self.types = types


class InterfaceDeclaration(SourceElement):
    _fields = ["name", "modifiers", "extends", "type_parameters", "body"]

    def __init__(
        self, name, modifiers=None, extends=None, type_parameters=None, body=None
    ):
        super(InterfaceDeclaration, self).__init__()
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


class EnumDeclaration(SourceElement):
    _fields = ["name", "implements", "modifiers", "type_parameters", "body"]

    def __init__(
        self, name, implements=None, modifiers=None, type_parameters=None, body=None
    ):
        super(EnumDeclaration, self).__init__()
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


class EnumConstant(SourceElement):
    _fields = ["name", "arguments", "modifiers", "body"]

    def __init__(self, name, arguments=None, modifiers=None, body=None):
        super(EnumConstant, self).__init__()
        if arguments is None:
            arguments = []
        if modifiers is None:
            modifiers = []
        if body is None:
            body = []
        self.name = name
        self.arguments = arguments
        self.modifiers = modifiers
        self.body = body


class AnnotationDeclaration(SourceElement):
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
        super(AnnotationDeclaration, self).__init__()
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


class AnnotationMethodDeclaration(SourceElement):
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
        super(AnnotationMethodDeclaration, self).__init__()
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


class TypeParameter(SourceElement):
    _fields = ["name", "extends"]

    def __init__(self, name, extends=None):
        super(TypeParameter, self).__init__()
        if extends is None:
            extends = []
        self.name = name
        self.extends = extends


class Expression(SourceElement):
    def __init__(self):
        super(Expression, self).__init__()


class BinaryExpression(Expression):
    _fields = ["operator", "lhs", "rhs"]

    def __init__(self, operator: str, lhs: SourceElement, rhs: SourceElement):
        super(BinaryExpression, self).__init__()
        self.operator = operator
        self.lhs = lhs
        self.rhs = rhs


class Assignment(BinaryExpression):
    pass


class Conditional(Expression):
    _fields = ["predicate", "if_true", "if_false"]

    def __init__(self, predicate, if_true, if_false):
        super(Conditional, self).__init__()
        self.predicate = predicate
        self.if_true = if_true
        self.if_false = if_false


class ConditionalOr(BinaryExpression):
    pass


class ConditionalAnd(BinaryExpression):
    pass


class Or(BinaryExpression):
    pass


class Xor(BinaryExpression):
    pass


class And(BinaryExpression):
    pass


class Equality(BinaryExpression):
    pass


class InstanceOf(BinaryExpression):
    pass


class Relational(BinaryExpression):
    pass


class Shift(BinaryExpression):
    pass


class Additive(BinaryExpression):
    pass


class Multiplicative(BinaryExpression):
    pass


class Unary(Expression):
    _fields = ["sign", "expression"]

    def __init__(self, sign, expression):
        super(Unary, self).__init__()
        self.sign = sign
        self.expression = expression


class Cast(Expression):
    _fields = ["target", "expression"]

    def __init__(self, target, expression):
        super(Cast, self).__init__()
        self.target = target
        self.expression = expression


class Statement(SourceElement):
    pass


class Empty(Statement):
    pass


class Block(Statement):
    _fields = ["statements"]

    def __init__(self, statements=None):
        super(Statement, self).__init__()
        if statements is None:
            statements = []
        self.statements = statements

    def __iter__(self):
        for s in self.statements:
            yield s


class VariableDeclaration(Statement, FieldDeclaration):
    pass


class ArrayInitializer(SourceElement):
    _fields = ["elements"]

    def __init__(self, elements: Optional[List[SourceElement]] = None):
        super(ArrayInitializer, self).__init__()
        if elements is None:
            elements = []
        self.elements = elements


class FuncCall(Expression):
    _fields = ["name", "arguments", "type_arguments", "target"]

    def __init__(self, name, arguments=None, type_arguments=None, target=None):
        super(FuncCall, self).__init__()
        if arguments is None:
            arguments = []
        if type_arguments is None:
            type_arguments = []
        self.name = name
        self.arguments = arguments
        self.type_arguments = type_arguments
        self.target = target


class IfThenElse(Statement):
    _fields = ["predicate", "if_true", "if_false"]

    def __init__(self, predicate, if_true, if_false=None):
        super(IfThenElse, self).__init__()
        self.predicate = predicate
        self.if_true = if_true
        self.if_false = if_false


class While(Statement):
    _fields = ["predicate", "body"]

    def __init__(self, predicate, body: Block):
        super(While, self).__init__()
        self.predicate = predicate
        self.body = body


class For(Statement):
    _fields = ["init", "predicate", "update", "body"]

    def __init__(self, init, predicate, update, body):
        super(For, self).__init__()
        self.init = init
        self.predicate = predicate
        self.update = update
        self.body = body


class ForEach(Statement):
    _fields = ["type", "variable", "iterable", "body", "modifiers"]

    def __init__(self, type, variable, iterable, body, modifiers=None):
        super(ForEach, self).__init__()
        if modifiers is None:
            modifiers = []
        self.type = type
        self.variable = variable
        self.iterable = iterable
        self.body = body
        self.modifiers = modifiers


class Assert(Statement):
    _fields = ["predicate", "message"]

    def __init__(self, predicate, message=None):
        super(Assert, self).__init__()
        self.predicate = predicate
        self.message = message


class Switch(Statement):
    _fields = ["expression", "switch_cases"]

    def __init__(self, expression, switch_cases: List["SwitchCase"]):
        super(Switch, self).__init__()
        self.expression = expression
        self.switch_cases = switch_cases

    def get_default_case(self) -> Optional["SwitchCase"]:
        for case in self.switch_cases:
            if isinstance(case.case, DefaultStatement):
                return case
        return None


class DefaultStatement(SourceElement):
    def __init__(self):
        super().__init__()


class SwitchCase(SourceElement):
    _fields = ["case", "body"]

    def __init__(
        self,
        case: Union[SourceElement, DefaultStatement],
        body: Union[Block, SourceElement],
    ):
        super(SwitchCase, self).__init__()
        self.case = case
        self.body = body


class DoWhile(Statement):
    _fields = ["predicate", "body"]

    def __init__(self, predicate, body: Block=None):
        super(DoWhile, self).__init__()
        self.predicate = predicate
        self.body = body


class Continue(Statement):
    _fields = ["label"]

    def __init__(self, label=None):
        super(Continue, self).__init__()
        self.label = label


class Break(Statement):
    _fields = ["label"]

    def __init__(self, label=None):
        super(Break, self).__init__()
        self.label = label


class Return(Statement):
    _fields = ["result"]

    def __init__(self, result=None):
        super(Return, self).__init__()
        self.result = result


class Synchronized(Statement):
    _fields = ["monitor", "body"]

    def __init__(self, monitor, body):
        super(Synchronized, self).__init__()
        self.monitor = monitor
        self.body = body


class Throw(Statement):
    _fields = ["exception"]

    def __init__(self, exception):
        super(Throw, self).__init__()
        self.exception = exception


class Try(Statement):
    _fields = ["block", "catches", "_finally", "resources"]

    def __init__(self, block, catches=None, _finally=None, resources=None):
        super(Try, self).__init__()
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


class Catch(SourceElement):
    _fields = ["variable", "modifiers", "types", "block"]

    def __init__(self, variable, modifiers=None, types=None, block=None):
        super(Catch, self).__init__()
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


class ConstructorInvocation(Statement):
    """An explicit invocations of a class's constructor.

    This is a variant of either this() or super(), NOT a "new" expression.
    """

    _fields = ["name", "target", "type_arguments", "arguments"]

    def __init__(self, name, target=None, type_arguments=None, arguments=None):
        super(ConstructorInvocation, self).__init__()
        if type_arguments is None:
            type_arguments = []
        if arguments is None:
            arguments = []
        self.name = name
        self.target = target
        self.type_arguments = type_arguments
        self.arguments = arguments


class InstanceCreation(Expression):
    _fields = ["type", "type_arguments", "arguments", "body", "enclosed_in"]

    def __init__(
        self, type, type_arguments=None, arguments=None, body=None, enclosed_in=None
    ):
        super(InstanceCreation, self).__init__()

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


class FieldAccess(Expression):
    _fields = ["name", "target"]

    def __init__(self, name: str, target: SourceElement):
        super(FieldAccess, self).__init__()

        self.name = name
        self.target = target


class ArrayAccess(Expression):
    _fields = ["index", "target"]

    def __init__(self, index, target):
        super(ArrayAccess, self).__init__()
        self.index = index
        self.target = target


class ArrayCreation(Expression):
    _fields = ["type", "dimensions", "initializer"]

    def __init__(self, type, dimensions=None, initializer=None):
        super(ArrayCreation, self).__init__()
        if dimensions is None:
            dimensions = []
        self.type = type
        self.dimensions = dimensions
        self.initializer = initializer


class Literal(SourceElement):
    _fields = ["value"]

    def __init__(self, value):
        super(Literal, self).__init__()
        self.value = value


class ClassLiteral(SourceElement):
    _fields = ["type"]

    def __init__(self, type):
        super(ClassLiteral, self).__init__()
        self.type = type


class Name(SourceElement):
    _fields = ["value"]

    def __init__(self, value: str):
        super(Name, self).__init__()
        self.value = value

    def append_name(self, name):
        try:
            self.value = self.value + "." + name.value
        except:
            self.value = self.value + "." + name


class ExpressionStatement(Statement):
    _fields = ["expression"]

    def __init__(self, expression):
        super(ExpressionStatement, self).__init__()
        self.expression = expression


# ===========================


class ReferenceExpr(Expression):
    _fields = ["value"]

    def __init__(self, value):
        super(ReferenceExpr, self).__init__()
        self.value = value


class DereferenceExpr(Expression):
    _fields = ["ref"]

    def __init__(self, ref):
        super(DereferenceExpr, self).__init__()
        self.ref = ref


class Label(SourceElement):
    _fields = ["name", "statement"]

    def __init__(self, name: str, stmt: Optional[SourceElement] = None):
        super(Label, self).__init__()
        self.name = name
        self.statement = stmt


class GoToStatement(SourceElement):
    _fields = ["label"]

    def __init__(self, label: str):
        super(GoToStatement, self).__init__()
        self.label = label


class Visitor(object):

    def __init__(self, verbose=False):
        self.verbose = verbose

    def __getattr__(self, name):
        
        if not (name.startswith("visit_") or name.startswith("leave_")):
            raise AttributeError(
                "name must start with visit_ or leave_ but was {}".format(name)
            )
        else:
            assert name.split("_")[1] in globals(), name
            
        def f(element):
            if self.verbose:
                msg = "unimplemented call to {}; ignoring ({})"
                print(msg.format(name, element))
            return True

        return f
