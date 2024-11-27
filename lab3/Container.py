from typing import List

from Component import Component


class Container(Component):

    def __init__(self):
        self._children : List[Component] = []

    def add(self, component: Component):
        self._children.append(component)
        component.parent = self

    def remove(self, component: Component):
        self._children.remove(component)
        component.parent = None

    def is_container(self) -> bool:
        return True

    def list(self) ->str:
        results = []
        for child in self._children:
            results.append(child.list())
        return f"Container({'+'.join(results)})"