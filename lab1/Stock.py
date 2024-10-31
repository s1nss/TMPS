import threading
from Ecigarette import Ecigarette


class Stock:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance.stock = []
        return cls._instance

    def add_product(self, ecigarette: Ecigarette):
        self.stock.append(ecigarette)

    def list_stock(self):
        for ecig in self.stock:
            print(ecig.details())
