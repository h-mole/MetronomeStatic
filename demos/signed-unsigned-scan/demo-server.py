import json
import os
import sys
from typing import cast

from PyBirdViewCode import abspath_from_current_file
from PyBirdViewCode.third_parties.jsonobject import (
    DictProperty,
    JsonObject,
    ObjectProperty,
)
from PyBirdViewCode.utils.service import BaseCommand, Problem, Server


class CommandData(JsonObject):
    range: dict = cast(dict, DictProperty())


class CBMCCommand(BaseCommand):
    data = ObjectProperty(CommandData)


class MyServer(Server):
    def handle_start_tool(self, command: CBMCCommand):
        print("command", command)
        checker_py_file = abspath_from_current_file("check.py", __file__)
        file_to_analyse = abspath_from_current_file("test.c", __file__)
        cmd = rf"{sys.executable} {checker_py_file} {file_to_analyse}"
        self.process_mgr.start_subprocess(
            "cbmc-routine", cmd, self.current_context.data_folder
        )

    def result_file(self):
        return "problems.json"

    def handle_task_finish(self):
        with open(
            os.path.join(self.current_context.data_folder, "problems.json"), "r"
        ) as f:
            self.current_context.found_problems = [
                Problem(item) for item in json.load(f)
            ]

    def handle_stop_tool(self, data: CBMCCommand):
        print("stopped!!!", data)
        self.process_mgr.stop_subprocess(
            "cbmc-routine",
        )


server = MyServer(CBMCCommand)
server.start()
print("started!")
