"""
Make a tool work as a distributed service

Pushing messages proactively

Distributed tool must know the endpoint of the scheduler.
"""

import json
import os
import sys
import threading
import time
import uuid
from typing import Generator, Generic, Optional, Tuple, Type, Union
import warnings

import websocket
from dataclasses import fields
from dataclasses_json import DataClassJsonMixin

from ..utils.files import file_to_dataurl
from ..utils import MelodieFrozenGenerator, melodie_generator
from .messages import RestRespDataType
from .base_request import Request, RequestFactory
from .log import logger
from .messages import FileUploadResponse, WSSchedulerMsgParser
from .models import (
    ProcessContext,
    Result,
    SchedulerCommandResponse,
    Status,
    StatusInfo,
    ToolMsgTypes,
    Trigger,
    WSSchedulerRawMsgType,
    WSToolRawMsgType,
)
from .processmgr import SubprocessManager


def dataclass_has_field(cls, field_name):
    return any(f.name == field_name for f in fields(cls))


class DistributedTool(Generic[RestRespDataType]):
    def __init__(
        self,
        cmd_data_type: Type[RestRespDataType],  # must have field `task_id`
        scheduler_addr: str,
        scheduler_port: int,
        name="default",
        root_folder=".PyBirdViewCode/tools_result",
    ) -> None:
        self.root_folder = root_folder
        if not os.path.exists(self.root_folder):
            os.makedirs(self.root_folder)
        assert dataclass_has_field(cmd_data_type, "task_id"), cmd_data_type
        self._cmd_data_type: Type[RestRespDataType] = cmd_data_type

        self.scheduler_endpoint = f"{scheduler_addr}:{scheduler_port}"
        self.name = name
        self._uuid = uuid.uuid4().hex
        self._ws = websocket.WebSocket()

        self._thread_websocket: threading.Thread

        self._thread_status_push = threading.Thread(target=self._task_status_push)
        self._thread_status_push.daemon = True

        self._thread_tasks_fetch = threading.Thread(target=self._task_process_tasks)
        self._thread_tasks_fetch.daemon = True

        self._requests = RequestFactory(scheduler_addr, scheduler_port)
        self._task_req: Request[RestRespDataType] = self._requests.create_request(
            "/api/tasks/get", self._cmd_data_type, timeout=1
        )
        self._upload_req: Request[FileUploadResponse] = self._requests.create_request(
            "/api/files/upload", FileUploadResponse, timeout=5
        )

        self.process_mgr = SubprocessManager(self.on_task_finish)

        self.current_context: Optional[ProcessContext] = (
            None  # ProcessContext(self.root_folder)
        )
        # Record the data for current task
        self.data_current_task: Optional[RestRespDataType] = None
        self._connect()

    def _connect(self):
        self._ws.connect(
            f"ws://{self.scheduler_endpoint}/api/websocket/{self.name}/{self._uuid}"
        )
        self._thread_websocket = threading.Thread(target=self._task_websocket)
        self._thread_websocket.daemon = True
        self._thread_websocket.start()

    def upload(self, file: str) -> Tuple[bool, str]:
        """
        Upload file
        """
        status, resp = self._upload_req.upload(file)
        if status < 299:
            assert resp.data is not None
            return True, resp.data.filename_in_storage
        else:
            return False, ""

    def _task_websocket(self):
        """
        Execute the background task for websocket.
        """
        parser = WSSchedulerMsgParser(self._cmd_data_type)
        while 1:
            try:
                msg: Union[str, bytes] = self._ws.recv()
            except ConnectionResetError as e:
                # When receiving this error, jump out of this `while` loop
                # then start a new listening thread.
                raise e
            try:
                data: WSSchedulerRawMsgType = json.loads(msg)
                parsed = parser.parse_scheduler_msg(data)
                raise NotImplementedError(parsed)
            except json.JSONDecodeError:
                warnings.warn(f"Cannot parse: {msg}")
                continue

    def _send_msg(self, type: ToolMsgTypes, data: DataClassJsonMixin):
        raw_msg: WSToolRawMsgType = {"type": type, "data": data.to_dict()}
        try:
            self._ws.send(json.dumps(raw_msg))
        except Exception:
            # TODO: Optimize the code for re-connect!
            logger.info("trying to reconnect...")
            try:
                self._connect()
            except Exception:
                logger.info("connection refused, retrying again...")
                import traceback

                traceback.print_exc()

    def _task_status_push(self):
        """
        Push status to the server
        """
        while 1:
            status = self.handle_status()
            self._send_msg("status", status)
            time.sleep(1)

    def _get_task(self):
        """
        Get task from scheduler
        """

    def running(self) -> bool:
        if self.current_context is None:
            return False
        return self.current_context.info.status == Status.RUNNING

    def _task_process_tasks(self):
        """
        Fetch and process tasks from the scheduler
        """
        logger.warning("started processing tasks!")
        while 1:
            if self.running():
                time.sleep(2)
                continue
            time.sleep(2)
            logger.info("before getting task!")
            try:
                status, resp = self._task_req.get({"tool_name": self.name})
                logger.info(f"fetching task {status} {resp}")
                if status < 299:
                    task_data = resp.data
                    self.data_current_task = task_data
                    self._task_start(task_data)
                else:
                    logger.debug(f"status: {status}, got msg: {resp.msg}")
            except Exception as e:
                import traceback

                traceback.print_exc()
                time.sleep(1)

    def on_task_finish(self, task_id: str):
        assert self.current_context is not None
        self.current_context.info.status = Status.STOPPED
        try:
            self.handle_task_finish()
            self._send_msg("result", self.get_result())
        except Exception:
            import traceback

            exc = traceback.format_exc()
            sys.stderr.write(exc)
            self.send_error(self.current_context, f"Finish task error: \n{exc}")

    def handle_task_finish(self):
        return

    def handle_status(self) -> StatusInfo:
        if self.current_context is not None:
            return self.current_context.info
        else:
            return StatusInfo(
                uuid="", start_time=-1, end_time=-1, status=Status.STOPPED
            )

    @melodie_generator
    def all_results(self) -> Generator[Tuple[str, StatusInfo], None, None]:
        for folder in os.listdir(self.root_folder):
            folder_abs_path = os.path.join(self.root_folder, folder)
            try:
                with open(
                    os.path.join(folder_abs_path, ".processinfo.json"), encoding="utf8"
                ) as f:
                    yield folder_abs_path, StatusInfo(**json.load(f))
            except Exception:
                import traceback

                traceback.print_exc()

    def results(self) -> MelodieFrozenGenerator[Tuple[str, StatusInfo]]:
        """
        Get all results, and sort by start time
        """
        return self.all_results().f.sort(lambda item: item[1].start_time, reverse=True)

    def get_result_additional_data(self) -> dict:
        return {}

    def get_result(self) -> Result:
        """
        Get the result produced during the latest running.
        """
        assert self.current_context is not None
        result_file = self.result_file()
        if result_file is not None:
            if not os.path.isabs(result_file):
                result_file = os.path.join(
                    self.current_context.data_folder, result_file
                )
            file_base64 = file_to_dataurl(result_file)
        else:
            file_base64 = "data:text/plain;base64,"  # empty file url
        return Result(
            task_id=self.current_context.task_id,
            info=self.current_context.info,
            problems=self.current_context.found_problems,
            raw_file=file_base64,
            additional_data=self.get_result_additional_data(),
        )

    def result_file(self) -> Optional[str]:
        return None

    def handle_results(self):
        return self.results().map(lambda x: x.to_json()).l

    def _task_start(self, task_data: RestRespDataType):
        try:
            self.current_context = ProcessContext(
                self.root_folder, task_data.task_id, uuid.uuid4().hex
            )
            self.handle_start_tool(task_data)
            self.current_context.info.status = Status.RUNNING
        except Exception as e:
            import traceback

            exc = traceback.format_exc()
            sys.stderr.write(exc)

            self.current_context.info.status = Status.FAILED
            self.send_error(self.current_context, str(e))

    def send_error(self, context: ProcessContext, msg: str):
        self._send_msg(
            "result",
            Result(
                context.task_id,
                info=context.info,
                problems=[],
                raw_file="",
                additional_data={},
                error=msg,
            ),
        )

    def process_command(self, cmd_uuid: str, cmd) -> SchedulerCommandResponse:
        """
        问题：如何解决Websocket的响应问题？
        """
        if cmd.type == Trigger.START:
            raise NotImplementedError

        elif cmd.type == Trigger.STOP:
            if self.current_context is None:
                return SchedulerCommandResponse(
                    cmd_uuid, False, "no process is running"
                )
            self.handle_stop_tool(cmd)
            self.current_context.info.status = Status.STOPPED
            self.current_context.info.end_time = time.time()
            self.current_context.dump()
            return SchedulerCommandResponse(cmd_uuid, True)
        else:
            raise NotImplementedError

    def handle_start_tool(self, cmd: RestRespDataType):
        """
        如果此方法中抛出异常，则会返回工具启动失败
        """
        raise NotImplementedError

    def handle_stop_tool(self, cmd: RestRespDataType):
        raise NotImplementedError

    def _start_tasks(self):
        self._thread_tasks_fetch.start()
        self._thread_status_push.start()

    def start(self):
        self._start_tasks()
        while True:
            time.sleep(1)

    def start_in_thread(self):
        self._start_tasks()
