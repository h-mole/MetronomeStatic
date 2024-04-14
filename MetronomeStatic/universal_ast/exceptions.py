from typing import Any


class FunctionReturn(Exception):
    def __init__(self, value: Any) -> None:
        self.value = value


class GoToLabel(Exception):
    def __init__(self, label: str) -> None:
        self.label = label
