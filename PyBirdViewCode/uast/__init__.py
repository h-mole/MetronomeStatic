import warnings
from .universal_ast_nodes import *
from .universal_cfg_extractor import (
    CFGBuilder,
    CFG,
    BasicBlock,
    remove_empty_node_from_cfg,
)
from .unparser import *
from .uast_queries import *
from .universal_code_property_graphs import (
    get_cdg_topology,
    get_ddg_topology,
    CodePropertyGraphs,
)

try:
    from .c_cpp_converter import ClangASTConverter
except ModuleNotFoundError as e:
    warnings.warn(
        f"C/CPP to UAST converter cannot be imported due to an import error: {e.msg}"
    )

try:
    from .python_converter import ParsoASTConverter
except ModuleNotFoundError as e:
    warnings.warn(
        f"Python to UAST converter cannot be imported due to an import error: {e.msg}"
    )
