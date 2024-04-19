import tests.base as base
from PyBirdViewCode.clang_utils import parse_file


def test_utils():
    try:
        parse_file("not-exist file!!")
        raise ValueError("should raise file not found error!")
    except FileNotFoundError:
        pass
    file = base.asset_path("extractor-demos/data-structure.cpp")
    parse_file(file, ["-xc++", "-std=c++11"])
    parse_file(file, ("-xc++", "-std=c++11"))
    parse_file(file, set(["-xc++", "-std=c++11"]))
    parse_file(
        file, lambda file: ["-xc++", "-std=c++11"] if file.endswith(".cpp") else []
    )
    try:
        parse_file(file, {})
        raise ValueError
    except NotImplementedError:
        pass
