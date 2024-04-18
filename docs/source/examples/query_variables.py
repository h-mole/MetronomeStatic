import sys

sys.path.append("../../..")
from MetronomeStatic import abspath_from_current_file
from MetronomeStatic.clang_utils import (
    get_func_decl,
    get_local_var_defs,
    get_var_refs,
    get_param_decls,
    get_global_ref_names,
    parse_file,
    get_func_decl,
    all_globals,
)


# Load file by clang and get the translation unit
translation_unit = parse_file(
    abspath_from_current_file("assets/query_variables.c", __file__)
)

# Get the cursor to whole file from Translation Unit
cursor = translation_unit.cursor

# Get the cursor to function demo_1
func_decl = get_func_decl(cursor, "demo_1")

## VARIABLE DECLARATIONS

# extract global variables defined in file
global_variables = all_globals(cursor).attributes("spelling").to_set()
print("Global variables:", global_variables)

# extract local variables
local_variables = get_local_var_defs(func_decl).attributes("spelling").to_set()
print("Local variables:", local_variables)

# extract parameters
param_variables = get_param_decls(func_decl).attributes("spelling").to_set()
print("Param variables:", param_variables)

## VARIABLE REFERENCES

# extract variable References
referenced_variables = get_var_refs(func_decl).attributes("spelling").to_set()
print("Referenced variables:", referenced_variables)


# extract global references
global_references = get_global_ref_names(func_decl).to_set()
print("Used global variables:", global_references)
