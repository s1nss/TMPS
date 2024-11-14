class ForeignEcig:
    def __init__(self, model_name, cost):
        self.model_name = model_name
        self.cost = cost

    def getName(self):
        return self.model_name

    def getCost(self):
        return self.cost
