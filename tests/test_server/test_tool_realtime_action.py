import os
import queue
import socket
import time
from dataclasses import dataclass
from typing import Optional, Type, TypedDict

from dataclasses_json import DataClassJsonMixin

from PyBirdViewCode.tools_service import DistributedTool, Problem, Scheduler


@dataclass
class MyCommand(DataClassJsonMixin):
    task_id: str
    path: str
    mode: str


class Tool(DistributedTool):
    data_current_task: MyCommand

    def handle_start_tool(self, data: MyCommand):
        self.task_data = data
        assert self.current_context is not None
        if os.name == "nt":
            cmd = "dir"
        else:
            cmd = "ls"

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
        return {
            "cmd_id": self.data_current_task.task_id,
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
    TOOLS_COUNT = 2
    TASKS_COUNT = 4

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
        self.scheduler._tasks["my-tool"] = queue.Queue()
        tasks = []
        for i in range(self.TASKS_COUNT):
            task = self.scheduler.execute_task(
                "my-tool",
                {
                    "task_id": f"{i}aac123aa",
                    "path": "AAA",
                    "mode": "BBB",
                    "git_version": "0acb...",
                },
            )
            tasks.append(task)
        for i in range(self.TASKS_COUNT):
            assert tasks[i].result().task_id == f"{i}aac123aa"

        print("trying to put another task..")
        self.scheduler.put_task(
            "my-tool", {"task_id": "0aac123aa", "path": "AAA", "mode": "acb"}
        )
        time.sleep(3)
        self.scheduler.get_result_with_id(f"0aac123aa")

        print("trying to put two tasks at the same time......")
        self.scheduler.put_task(
            "my-tool", {"task_id": "0aac123ab", "path": "AAA", "mode": "acb"}
        )
        self.scheduler.put_task(
            "my-tool", {"task_id": "1aac123ab", "path": "AAA", "mode": "acb"}
        )
        time.sleep(10)
        print(self.scheduler._results.qsize())
        results = self.scheduler.get_task_results({f"0aac123aa", f"1aac123ab"})
        assert len(results) == 2
