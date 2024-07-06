from PyBirdViewCode.algorithms.pointer_analysis_interproc_ctx import (
    CallSiteSensitivePointerAnalysis,
)
from PyBirdViewCode import get_file_uast, FileManager, abspath_from_file, uast
from tests.base import asset_path
from PyBirdViewCode.uast.builtin_converters.python_converter import (
    UASTTypeInfer,
)
from dataclasses import dataclass
from typing import Literal, Optional

fm = FileManager(abspath_from_file("output", __file__))


@dataclass
class VarScope:
    name: str
    kind: Literal["class", "function", "global"]
    context: dict[str, str]
    types_mapping: dict[str, str]

    def get_cls_and_method(self):
        """
        将name分割为类名和方法名称
        """
        return self.name.rsplit(".", 1)


class VarScopeMgr:
    class VarScopeCtxMgr:
        def __init__(self, var_scope_mgr, name, kind) -> None:
            self.var_scope_mgr: VarScopeMgr = var_scope_mgr
            self.kind = kind
            self.name = name

        def __enter__(self):
            self.var_scope_mgr.scopes_stack.append(
                VarScope(self.name, self.kind, {}, {})
            )
            self.var_scope_mgr.level += 1

        def __exit__(self, exc_type, exc_value, traceback):
            self.var_scope_mgr.scopes_stack.pop()
            self.var_scope_mgr.level -= 1

    def __init__(self) -> None:
        self.scopes_stack: list[VarScope] = [VarScope("", "global", {}, {})]
        self.level = 0

    @property
    def top_scope(self) -> VarScope:
        return self.scopes_stack[-1]

    def scope_from_top(self, level_no: int = 1) -> VarScope:
        """
        :level_no: 1表示当前作用域（倒数第一层），2表示上一级作用域（倒数第二层），依此类推
        """
        return self.scopes_stack[len(self.scopes_stack) - level_no]

    def get_context_manager(
        self, name: str, kind: Literal["class", "function", "global"]
    ):
        """
        :name: 类/函数/方法的名称。如果是方法, 则写C.id
        :kind: 该变量管理的类型
        """
        return VarScopeMgr.VarScopeCtxMgr(self, name, kind)

    def lookup_variable_type(self, name: str) -> Optional[uast.DATA_TYPE]:
        for scope in reversed(self.scopes_stack):
            if name in scope.variables:
                return scope.variables[name]

    def __repr__(self) -> str:
        s = ", ".join([f"{k}={v}" for k, v in self.__dict__.items()])
        return f"<{self.__class__.__name__} {s}>"


class PAConverter:
    def __init__(self) -> None:
        self.call_stack = VarScopeMgr()

    def resolve_type(self, node: uast.SourceElement) -> str:

        match node:
            case uast.Name(id=var_name):
                if var_name == "this":
                    # current_variable代表调用方法时，对象的名称
                    # 如obj.m()中，current_variable="obj"
                    cls, method = self.call_stack.top_scope.name.split(".")
                    return cls
                else:
                    return self.call_stack.top_scope.types_mapping[var_name]
            case uast.UnaryExpr():
                return self.resolve_type(node.expression)
            case _:
                raise NotImplementedError(node)

    def resolve_method(self, node: uast.SourceElement) -> str:
        """
        输入相应的uast节点，返回对应的方法，如C.main
        """
        match node:
            case uast.FieldAccessExpr(name=field_name):
                target_type = self.resolve_type(node.target)
                return f"{target_type}.{field_name}"
            case _:
                raise NotImplementedError(node)

    def get_type_text(self, type: uast.DATA_TYPE) -> str:
        match type:
            case uast.AddrReferenceType():
                return self.get_type_text(type.referee)
            case uast.ClassType() | uast.StructType() | uast.UserDefinedType():
                return type.name
            case _:
                raise NotImplementedError(type)

    def extract_methods(self, method_uast: uast.MethodDecl):
        assert method_uast.body is not None
        for stmt in method_uast.body.walk_preorder():
            match stmt:
                case uast.VarDecl(
                    variable=uast.Name(id=var_name), type=var_type, location=(line, _)
                ):
                    print(var_name, var_type, line)
                    self.call_stack.top_scope.context[f"o_l_{line}"] = (
                        var_name,
                        self.get_type_text(var_type),
                    )
                    self.call_stack.top_scope.types_mapping[var_name] = (
                        self.get_type_text(var_type)
                    )
        called_methods = []
        for stmt in method_uast.body.walk_preorder():
            match stmt:
                case uast.CallExpr(location=(line, _)):
                    called_method = self.resolve_method(stmt.name)
                    called_methods.append(called_method)
        for method in called_methods:
            with self.call_stack.get_context_manager(method, "function"):
                cls_name, method_name = method.rsplit(".", 1)
                class_uast = _uast.filter_by(uast.ClassDecl, name=cls_name).head()
                method_uast = (
                    class_uast.filter_by(uast.MethodDecl)
                    .filter(lambda method: method.name.id == method_name)
                    .head()
                )
                self.extract_methods(method_uast)

        # print(called_methods)
        print(self.call_stack.scopes_stack)


def test_pointer_analysis():
    global _uast
    py_file = asset_path("algorithms-demo/pointer-example.cpp")
    _uast = get_file_uast(py_file)
    fm.json_dump(_uast.to_dict(), "pointer-example-uast.json")

    class_c_uast = _uast.filter_by(uast.ClassDecl, name="C").head()
    main_method = (
        class_c_uast.filter_by(uast.MethodDecl)
        .filter(lambda method: method.name.id == "main")
        .head()
    )
    conv = PAConverter()
    conv.extract_methods(main_method)
