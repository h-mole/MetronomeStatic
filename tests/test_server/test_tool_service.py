import os
import queue
import socket
import time
from dataclasses import dataclass

from dataclasses_json import DataClassJsonMixin

from PyBirdViewCode.tools_service import DistributedTool, Problem, Scheduler


@dataclass
class MyCommand(DataClassJsonMixin):
    path: str
    mode: str


class Tool(DistributedTool):
    def handle_start_tool(self, data: MyCommand):
        print("started to process", data)
        assert self.current_context is not None
        if os.name == "nt":
            cmd = "ping -n 3 127.0.0.1> out.txt"
        else:
            cmd = "ping -c 3 127.0.0.1> out.txt"
        self.process_mgr.start_subprocess(
            "cbmc-routine",
            cmd,
            self.current_context.data_folder,
        )
        print("tool process started!", self._uuid)

    def handle_stop_tool(self, data: MyCommand):
        self.process_mgr.stop_subprocess(
            "cbmc-routine",
        )
        # self.current_context

    def get_result_additional_data(self) -> dict:
        return {"taskId": "aac123aa"}

    def handle_task_finish(self):
        self.current_context.found_problems = [
            Problem.from_dict(
                {
                    "file": "C:\\Users\\houzh\\Developing\\PyBirdViewCode\\demos\\board-type\\test.c",
                    "description": "存在从有符号型整数到无符号型整数的隐式转换，可能存在类型问题。",
                    "position": {
                        "type": "line_col",
                        "line": 4,
                        "column": 18,
                        "text": None,
                    },
                }
            )
        ]
        self.upload(__file__)

    def result_file(self) -> str:
        return "out.txt"


def find_unused_port() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("", 0))
        s.listen(1)
        port = s.getsockname()[1]
    return port


class TestTool:
    TOOLS_COUNT = 2
    TASKS_COUNT = 6

    def setup_class(self):
        port = find_unused_port()
        self.scheduler = Scheduler(port=port)
        self.scheduler.start_in_thread()

        time.sleep(4)

        self.tools = [
            Tool(MyCommand, "localhost", port, "default-tool")
            for i in range(self.TOOLS_COUNT)
        ]
        for tool in self.tools:
            tool.start_in_thread()

    def teardown_class(self):
        print("清理。。。")

    def test_assign_task(self):
        for i in range(self.TASKS_COUNT):
            if "default-tool" not in self.scheduler._tasks:
                self.scheduler._tasks["default-tool"] = queue.Queue()
            self.scheduler._tasks["default-tool"].put({"path": "AAA", "mode": "BBB"})

        for i in range(self.TASKS_COUNT):
            result = self.scheduler._results.get(timeout=10)
            print("result", result)
            assert result.additional_data["taskId"] == "aac123aa"
        assert self.scheduler._results.empty()
        # print(result)
