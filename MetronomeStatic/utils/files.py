import base64
import json
import mimetypes
import os
from typing import Any
import networkx as nx


def parse_dataurl(dataurl: str):
    """
    解析前端传来的dataurl
    """
    if not dataurl.startswith("data:"):
        raise ValueError("Invalid DataURL")

    # 提取 MIME 类型和编码后的数据
    mime_type, encoded_data = dataurl[5:].split(";base64,", 1)

    # 解码数据
    decoded_data = base64.b64decode(encoded_data)

    return mime_type, decoded_data


def file_to_dataurl(file_path: str):
    """
    将文件转为dataurl
    """
    mimetype, _ = mimetypes.guess_type(file_path, strict=True)
    with open(file_path, "rb") as file:
        file_content = file.read()
        data_url = base64.b64encode(file_content).decode("ascii")

        return f"data:{mimetype};base64,{data_url}"


def abspath_from_current_file(rel_path: str, current_file: str) -> str:
    """
    Convert the relative path to absolute path.

    TODO: Deprecated method
    """
    return os.path.abspath(
        os.path.join(
            os.path.dirname(current_file),
            rel_path,
        )
    )


def abspath_from_file(rel_path: str, file: str) -> str:
    """
    Convert the relative path to absolute path.
    """
    return os.path.abspath(
        os.path.join(
            os.path.dirname(file),
            rel_path,
        )
    )


def decorator_path_ensure(func):
    def wrapper(self: "FileManager", file_relpath, *args, **kwargs):
        dirname = os.path.dirname(self.get_abspath(file_relpath))
        if not os.path.exists(dirname) and self.auto_create_folder:
            os.makedirs(dirname)
        result = func(self, file_relpath, *args, **kwargs)
        return result

    return wrapper


class FileManager:
    def __init__(self, base_dir: str, auto_create_folder=True) -> None:
        self.dir = os.path.abspath(base_dir)
        self.auto_create_folder = auto_create_folder
        if self.auto_create_folder:
            self.ensure_folder_exist(self.dir)
        assert os.path.exists(self.dir)

    def get_abspath(self, file_relpath: str) -> str:
        return os.path.abspath(os.path.join(self.dir, file_relpath))

    def ensure_folder_exist(self, folder_path: str):
        folder_path = self.get_abspath(folder_path)
        if self.auto_create_folder:
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

    def json_load(self, file_relpath: str):
        """
        Load json from file
        """
        file = self.get_abspath(file_relpath)
        with open(file, "r") as f:
            return json.load(f)

    @decorator_path_ensure
    def json_dump(self, file_relpath: str, data: Any, indent=2, ensure_ascii=False):
        """
        Dump json to file.
        Be careful that the `ensure_ascii` parameter was `False` by default,
          different from the standard library `json`.
        """
        assert file_relpath.endswith(".json"), "extension should be *.json"
        file = self.get_abspath(file_relpath)
        with open(file, "w") as f:
            json.dump(data, f, indent=indent, ensure_ascii=ensure_ascii)

    @decorator_path_ensure
    def dot_dump(self, file_relpath: str, graph: nx.Graph):
        """
        Dump networkx graph to dot file.
        """
        assert file_relpath.endswith(".dot"), "extension should be *.dot"
        file = self.get_abspath(file_relpath)
        nx.nx_pydot.write_dot(graph, file)
