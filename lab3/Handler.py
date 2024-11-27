from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional


class Handler(ABC):


    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass


class AbstractHandler(Handler):

    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: Any) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)

        return None


class AgeHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Age":
            return f"Pass the {request} test"
        else:
            return super().handle(request)

class GenderHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Gender":
            return f"Pass the {request} test"
        else:
            return super().handle(request)

class HeterosexualityHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Heterosexuality":
            return f"Pass the {request} test"
        else:
            return super().handle(request)


