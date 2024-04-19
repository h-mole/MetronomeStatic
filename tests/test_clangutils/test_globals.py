import tests.base as base
from PyBirdViewCode.clang_utils import (
    all_globals,
    get_func_decl_all,
    get_global_refs,
)


def test_extract_globals():
    c = base.clangutils_load_ast("extractor-demos/globals.c")
    global_names = {_global.spelling for _global in all_globals(c)}
    assert "not_global" not in global_names


def test_get_global_uses():
    c = base.clangutils_load_ast("extractor-demos/global-use.c")
    global_var_names = all_globals(c).attributes("spelling").to_set()
    funcs = get_func_decl_all(c, True).to_list()
    for f in funcs:
        print(f.spelling)
        global_refs = (
            get_global_refs(f)
            .filter(lambda x: x.spelling in global_var_names)
            .attributes("spelling")
            .to_list()
        )
        print(global_refs)
