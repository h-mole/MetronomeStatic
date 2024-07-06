import uuid
from abc import ABCMeta, abstractmethod
from typing import Any, Type
from PyBirdViewCode import uast


class BaseASTExtractor(metaclass=ABCMeta):
    """Base class for loading programming language file
    and convert it to AST"""

    def __init__(self, file: str, extra_args: list[str]) -> None:
        self.file = file
        self.extra_args = extra_args

    @classmethod
    @abstractmethod
    def supported_file_types(cls) -> list[str]:
        """
        可以应用于的文件类型列表

        :filename: 文件的绝对路径
        :return: 该AST抽取类是否可抽取该文件
        """
        pass

    @abstractmethod
    def extract_ast(self) -> tuple[tuple[Any, dict], list[str]]:
        """
        从源代码中提取AST

        :return: 两个参数，第一个是一个元组，为 `(AST对象, 用于UASTConverter其他辅助信息)`，
            第二个是错误信息的列表
        """
        pass


class BaseUASTConverter(metaclass=ABCMeta):
    """Base converter class from original AST to UAST"""

    def __init__(self, **kwargs) -> None:
        pass

    @classmethod
    @abstractmethod
    def supported_ast_types(cls) -> list[Type]:
        """
        返回可以应用的抽象语法树对象类型

        :return: 该UAST转换类支持的所有抽象语法树对象类型
        """
        pass

    @abstractmethod
    def convert_to_uast(self, original_ast: Any) -> uast.SourceElement:
        """将某个语言的AST转换为UAST"""
        pass

    def create_temporary_variable_name(self, prefix: str) -> str:
        return prefix + str(uuid.uuid4())[:5]
