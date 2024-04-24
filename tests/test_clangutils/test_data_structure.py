from typing import Generator

from PyBirdViewCode.clang_utils.code_attributes.utils import parse_file
import tests.base as base
from PyBirdViewCode import MelodieFrozenGenerator, MelodieGenerator
from PyBirdViewCode.clang_utils import (
    ClassDefModel,
    Cursor,
    CursorKind,
    DefModel,
    FieldDefModel,
    FunctionDefModel,
    StructDefModel,
    TraversalContext,
    UnionDefModel,
    beautified_print_ast,
    build_call_graph,
    data_structure_from_file,
    iter_data_structures,
    program_model_unparse,
    traversal,
)


def extract_tasks(c: Cursor):
    for child in c.walk_preorder():
        if child.kind == CursorKind.CALL_EXPR and child.spelling == "start_task":
            children: Generator[Cursor, None, None] = child.get_children()
            param = MelodieGenerator(children).slice(1).head()
            print("spelling", param.spelling)


def test_generate_structure():
    structures: MelodieFrozenGenerator[DefModel] = data_structure_from_file(
        base.asset_path("extractor-demos/global-use.c")
    ).f
    union_wrapper: StructDefModel = structures.filter(
        lambda s: s.spelling == "MyUnionWrapper" and isinstance(s, StructDefModel)
    ).head()
    field_classes = union_wrapper.iter_fields.map(
        lambda field: field.__class__
    ).to_list()
    assert len(field_classes) == 1 and issubclass(field_classes[0], UnionDefModel)
    l = structures.map(lambda item: item.to_serializable_dict()).to_list()

    extract_tasks(base.clangutils_load_ast("extractor-demos/global-use.c"))


def test_process_real_preprocessed_file():
    structures = iter_data_structures(
        base.asset_path("lua-preprocessed-code"),
        lambda name: name.endswith((".i")),
    ).freeze()


def test_iter_data_structures():
    structures = iter_data_structures(
        base.asset_path("structure-demo"),
        lambda name: name.endswith((".c", ".cpp", ".h")),
    ).freeze()
    result = {"referenced_globals": {}, "callings": {}}

    def reduce_f(orig: dict, model: FunctionDefModel):
        orig["referenced_globals"][model.spelling] = model.referenced_globals
        orig["callings"][model.spelling] = model.callings
        return orig

    output = (
        structures.filter(lambda structure: isinstance(structure, FunctionDefModel))
        .cast(FunctionDefModel)
        .reduce(reduce_f, result)
    )
    print("output", output)
    g = build_call_graph(output["callings"])
    print(g)


def test_data_structure():
    c = base.clangutils_load_ast("extractor-demos/data-structure.cpp")
    traversal(c).slice(
        5, 6
    ).head().print_hierarchy()  # ensure this step will not raise error
    try:
        TraversalContext().current_node
    except ValueError:
        pass
    ctxs = traversal(c).filter(
        lambda ctx: ctx.current_node.kind == CursorKind.STRUCT_DECL
    )
    head = ctxs.head()
    c = StructDefModel.from_cursor(head.current_node)
    print(c.to_serializable_dict())


def test_class_structure():
    c = base.clangutils_load_ast(
        "extractor-demos/data-structure.cpp", ["-xc++", "-std=c++11"]
    )
    ctxs = traversal(c).filter(
        lambda ctx: ctx.current_node.kind == CursorKind.CLASS_DECL
        and ctx.current_node.spelling == "Box"
    )

    head = ctxs.head()
    c = ClassDefModel.from_cursor(head.current_node)
    beautified_print_ast(head.current_node, "out.json")
    # print(c.to_serializable_dict())
    c.iter_fields.map(lambda x: print(x.to_serializable_dict())).exhaust()
    c.iter_methods.map(lambda x: print(x.to_serializable_dict())).exhaust()
    # c.iter_methods.map(lambda x: print(x.to_serializable_dict())).exhaust()


def test_unparse():
    d1 = {
        "class": "FieldDefModel",
        "spelling": "length",
        "type": {
            "class": "TypeWrapper",
            "_type": None,
            "spelling": "double",
            "kind": "TypeKind.DOUBLE",
        },
        "init_value_text": "",
    }

    sdm: FieldDefModel = program_model_unparse(d1)
    assert isinstance(sdm, FieldDefModel)
    assert sdm.spelling == "length"
    assert sdm.type.spelling == "double"

    d2 = {
        "class": "FunctionDefModel",
        "spelling": "set",
        "type": {
            "class": "TypeWrapper",
            "_type": None,
            "spelling": "void (double, double, double)",
            "kind": "TypeKind.FUNCTIONPROTO",
        },
        "location": [
            "C:\\Users\\houzh\\Developing\\PyBirdViewCode\\tests\\assets\\structure-demo\\header.h",
            2,
            5,
        ],
        "params": [
            {
                "class": "ParamDefModel",
                "spelling": "len",
                "type": {
                    "class": "TypeWrapper",
                    "_type": None,
                    "spelling": "double",
                    "kind": "TypeKind.DOUBLE",
                },
            },
            {
                "class": "ParamDefModel",
                "spelling": "bre",
                "type": {
                    "class": "TypeWrapper",
                    "_type": None,
                    "spelling": "double",
                    "kind": "TypeKind.DOUBLE",
                },
            },
            {
                "class": "ParamDefModel",
                "spelling": "hei",
                "type": {
                    "class": "TypeWrapper",
                    "_type": None,
                    "spelling": "double",
                    "kind": "TypeKind.DOUBLE",
                },
            },
        ],
        "callings": ["aaa", "bbb"],
    }
    sdm: FunctionDefModel = program_model_unparse(d2)
    assert isinstance(sdm, FunctionDefModel)
    assert sdm.spelling == "set"
    assert sdm.iter_params.attributes("spelling").to_set() == {"hei", "bre", "len"}
    assert sdm.iter_params.attributes("type").attributes("spelling").to_set() == {
        "double"
    }
    assert sdm.iter_callings.to_list() == ["aaa", "bbb"]
    assert sdm.location[1] == 2


class MyDefModel(DefModel):
    def __init__(self) -> None:
        super().__init__("")
        self.data = {"asd": "aosd"}
        self.set = {"aaa", "bbb"}


def test_structure_basics():
    ret = DefModel.from_serializable_dict({"asd": "psdkasda"})
    assert isinstance(ret, dict)

    serializable_dict = MyDefModel().to_serializable_dict()
    assert serializable_dict["data"]["asd"] == "aosd"

    repr(MyDefModel())  # make sure __repr__ method will not raise error

    try:
        MyDefModel.from_cursor(None)
        raise ValueError("should raise exception")
    except NotImplementedError:
        pass
    print(serializable_dict)
