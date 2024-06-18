from tests.base import asset_path
from PyBirdViewCode.utils import convert_encodings, abspath_from_file, FileManager

file_manager = FileManager(abspath_from_file("output", __file__))


def test_convert_encodings():
    folder_abs_path = asset_path("gb2312-encoding-folder")
    convert_encodings(
        folder_abs_path,
        lambda f: f.endswith((".c", ".h")),
        "gb2312",
        "utf8",
        file_manager.get_abspath("utf8-encoding-folder"),
    )
