from __future__ import annotations

from abc import ABC, abstractmethod


class Component(ABC):

    def __init__(self):
        super().__init__()
        self._parent = None

    @property
    def parent(self) -> Component:
        return self._parent

    @parent.setter
    def parent(self, parent: Component):
        self._parent = parent

    def add(self, component: Component):
        pass

    def remove(self, component: Component):
        pass

    def is_container(self) -> bool:
        return False


    @abstractmethod
    def list(self)->str:
        pass

