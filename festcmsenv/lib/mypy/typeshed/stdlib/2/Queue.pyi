# Stubs for Queue (Python 2)

from typing import Any, TypeVar, Generic, Optional

_T = TypeVar('_T')

class Empty(Exception): ...
class Full(Exception): ...

class Queue(Generic[_T]):
    maxsize = ... # type: Any
    mutex = ... # type: Any
    not_empty = ... # type: Any
    not_full = ... # type: Any
    all_tasks_done = ... # type: Any
    unfinished_tasks = ... # type: Any
    def __init__(self, maxsize: int = ...) -> None: ...
    def task_done(self) -> None: ...
    def join(self) -> None: ...
    def qsize(self) -> int: ...
    def empty(self) -> bool: ...
    def full(self) -> bool: ...
    def put(self, item: _T, block: bool = ..., timeout: Optional[float] = ...) -> None: ...
    def put_nowait(self, item: _T) -> None: ...
    def get(self, block: bool = ..., timeout: Optional[float] = ...) -> _T: ...
    def get_nowait(self) -> _T: ...

class PriorityQueue(Queue): ...
class LifoQueue(Queue): ...
