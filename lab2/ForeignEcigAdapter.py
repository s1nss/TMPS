from lab2.Ecigarette import Ecigarette
from lab2.ForeignEcig import ForeignEcig

class ForeignEcigAdapter(Ecigarette):
    def __init__(self, foreign_ecig: ForeignEcig):
        self._foreign_ecig = foreign_ecig

    @property
    def name(self):
        return self._foreign_ecig.getName()

    @property
    def price(self):
        return self._foreign_ecig.getCost()

    def list(self):
        return f"Foreign E-cigarette - {self.name}: ${self.price}"
