import os
import queue
import socket
import time
from dataclasses import dataclass

from dataclasses_json import DataClassJsonMixin

from PyBirdViewCode.tools_service import DistributedTool, Scheduler


@dataclass
class MyCommand(DataClassJsonMixin):
    task_id: str
    path: str
    mode: str


class Tool(DistributedTool):
    data_current_task: MyCommand

    def handle_start_tool(self, data: MyCommand):
        return {}["abc"]  # will raise key error

    def handle_stop_tool(self, data: MyCommand):
        self.process_mgr.stop_subprocess(
            "cbmc-routine",
        )
        # self.current_context

    def get_result_additional_data(self) -> dict:
        return {
            "cmd_id": self.data_current_task.cmd_id,
            "taskId": "aac123aa",
            "data": 123,
            # "current_task_data": self.data_current_task,
        }

    def handle_task_finish(self):

        pass


def find_unused_port() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("", 0))
        s.listen(1)
        port = s.getsockname()[1]
    return port


class TestTool:
    TOOLS_COUNT = 1
    TASKS_COUNT = 1

    def setup_class(self):
        port = find_unused_port()
        self.scheduler = Scheduler(port=port)
        self.scheduler.start_in_thread()

        time.sleep(3)

        self.tools = [
            Tool(MyCommand, "localhost", port, "my-tool")
            for i in range(self.TOOLS_COUNT)
        ]
        for tool in self.tools:
            tool.start_in_thread()

    def teardown_class(self):
        print("清理。。。")

    def test_assign_task(self):
        # for i in range(self.TASKS_COUNT):
        #     if "my-tool" not in self.scheduler._tasks:
        self.scheduler._tasks["my-tool"] = queue.Queue()
        self.scheduler.put_task(
            "my-tool",
            {
                "task_id": "aac123aa",
                "path": "AAA",
                "mode": "BBB",
                "git_version": "0acb...",
            },
        )

        # for i in range(self.TASKS_COUNT):
        result = self.scheduler._results.get(timeout=10)
        assert result.task_id == "aac123aa"
        assert self.scheduler._results.empty()
