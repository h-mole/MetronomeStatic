"""
此文件中定义运用UAST进行代码分析的命令
"""

import os
from typing import List, Type, Union, cast, Optional
from .universal_ast_nodes import CompilationUnit, MethodDecl
from .builtin_converters import (
    BaseASTExtractor,
    BaseUASTConverter,
    ClangASTConverter,
    ClangASTExtractor,
    ParsoASTConverter,
    ParsoASTExtractor,
)
from .universal_cfg_extractor import CFGBuilder, CFG
from .universal_code_property_graphs import CodePropertyGraphs
import logging

logger = logging.getLogger("PBVC_DIAGNOSTICS")

_ast_extractors: dict[str, Type[BaseASTExtractor]] = {
    # ClangASTExtractor,
}

_uast_converters: dict[Type, Type[BaseUASTConverter]] = {
    # ClangASTConverter
}


def register_converter(
    language: str,
    ast_extractor_type: Type[BaseASTExtractor],
    uast_converter_type: Type[BaseUASTConverter],
):
    for file_ext in ast_extractor_type.supported_file_types():
        if not file_ext.startswith("."):
            file_ext = "." + file_ext
        _ast_extractors[file_ext] = ast_extractor_type
    for ast_type in uast_converter_type.supported_ast_types():
        _uast_converters[ast_type] = uast_converter_type


def get_file_uast(file: str, extra_args: List[str] = []) -> CompilationUnit:
    """
    从文件中直接抽取UAST
    :file: 代码文件名
    :extra_args: 额外参数，直接传递给相应语言的AST解析器
    """
    # splitext产生的文件名一定会有.开头
    _, ext = os.path.splitext(file)
    if ext not in _ast_extractors:
        raise ValueError(f"Unsupported file extension: {ext}")
    extractor = _ast_extractors[ext](file, extra_args)
    ast, diags = extractor.extract_ast()
    for item in diags:
        logger.warning(item)
    for ast_type, converter_cls in _uast_converters.items():
        if isinstance(ast, ast_type):
            uast = cast(CompilationUnit, converter_cls().convert_to_uast(ast))
            return uast
    raise TypeError(f"No converter found for AST type: {type(ast)}")


def extract_cfg_from_method(method_or_func: MethodDecl) -> CFG:
    """
    从uast的Method中，抽取控制流图CFG
    """
    cfg_builder = CFGBuilder()
    cfg = cfg_builder.build(method_or_func)
    return cfg


def get_method_cpg(
    method_or_func: MethodDecl, extra_variables: Optional[list[str]] = None
) -> CodePropertyGraphs:
    """
    从uast的Method中，抽取代码属性图（Code Property Graphs, CPG），包含CFG、DDG、CDG and PDG

    :extra_variables: 在进行数据依赖分析时，除了函数的参数，还要额外考虑的变量。比如全局变量或者类的属性等。
    """
    extra_variables = extra_variables or []
    return CodePropertyGraphs(method_or_func, extra_variables)


def _register_builtin_converters():
    register_converter("c/cpp", ClangASTExtractor, ClangASTConverter)
    register_converter("python3", ParsoASTExtractor, ParsoASTConverter)


_register_builtin_converters()
