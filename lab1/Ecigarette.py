from abc import ABC, abstractmethod

class Ecigarette(ABC):
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price



    @abstractmethod
    def details(self):
        pass

# Concrete product types
class StarterKit(Ecigarette):
    def details(self):
        return f"Starter Kit - {self.name}: ${self.price}"

class AdvancedKit(Ecigarette):
    def details(self):
        return f"Advanced Kit - {self.name}: ${self.price}"

class Disposable(Ecigarette):
    def details(self):
        return f"Disposable E-cigarette - {self.name}: ${self.price}"
