from typing import Any

class reify:
    def __init__(self, wrapped: Any) -> None: ...
    def __get__(self, inst: Any, owner: Any) -> Any: ...
    def __set__(self, inst: Any, value: Any) -> None: ...
