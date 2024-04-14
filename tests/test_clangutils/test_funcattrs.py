import tests.base as base
from MetronomeStatic.clang_utils import (
    get_func_decl,
    get_func_decl_all,
    get_global_ref_names,
    get_local_var_defs,
    get_param_decls,
    get_var_refs,
)


def test_extract_funcs():
    c = base.clangutils_load_ast("extractor-demos/func_defs_decls.c")
    func_decl = get_func_decl_all(c).map(lambda x: x.spelling).to_list()
    assert len(func_decl) == 3 and len(set(func_decl)) == 2
    func_decl = (
        get_func_decl_all(c, definition_only=True)
        .filter(lambda x: x.spelling == "myfun")
        .to_list()
    )
    assert len(func_decl) == 1
    ret = get_var_refs(func_decl[0], True).to_list()
    assert len(ret) == 1 and ret[0].spelling == "fun"


def test_extract_func_attrs():
    c = base.clangutils_load_ast("extractor-demos/globals.c")
    assert get_func_decl(c, "not_existing_func") is None
    func_decl = get_func_decl(c, "use_global")

    # extract local variables
    local_vars = get_local_var_defs(func_decl).attributes("spelling").freeze()
    _ = local_vars.to_set()
    assert {"c", "x"} == local_vars.to_set()

    # extract referenced variables
    assert {"p", "y", "a", "b"} == get_var_refs(func_decl).attributes(
        "spelling"
    ).to_set()

    # extract referenced variables with functions
    assert {"p", "y", "a", "b", "f"} == get_var_refs(
        func_decl, include_funcs=True
    ).attributes("spelling").to_set()

    # extract parameter variables
    assert {"y", "z"} == get_param_decls(func_decl).attributes("spelling").to_set()

    # extract all global values
    assert {"a", "p", "b"} == get_global_ref_names(func_decl).to_set()
