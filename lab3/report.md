# Behavioral Design Patterns

## Author: Vlad Pruteanu

----

## Objectives:
1. Study and understand the Behavioral Design Patterns.
2. As a continuation of the previous laboratory work, think about what communication between software entities might be involed in your system.
3. Implement some additional functionalities using behavioral design patterns.
  


## Used Design Patterns:
* Chain of responsibility - allows passing request along the chain of potential handlers until one of them handles request


## Implementation

### Chain of responsibility
- The code implements a Chain of Responsibility design pattern, where requests are passed through a sequence of handlers, each processing or forwarding the request based on specific conditions.

```python
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



```



## Conclusions / Screenshots / Results


In this laboratory, we explored the Chain of Responsibility design pattern, which is a behavioral design pattern. It is used to pass requests along a chain of handlers, where each handler decides whether to process the request or pass it to the next handler in the chain. This decouples the sender and receiver of the request, making the system more flexible and scalable.

