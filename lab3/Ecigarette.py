
from Component import Component


class Ecigarette(Component):
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def list(self):
        pass



class StarterKit(Ecigarette):
    def list(self):
        return f"Starter Kit - {self.name}: ${self.price}"

class AdvancedKit(Ecigarette):
    def list(self):
        return f"Advanced Kit - {self.name}: ${self.price}"

class Disposable(Ecigarette):
    def list(self):
        return f"Disposable E-cigarette - {self.name}: ${self.price}"
