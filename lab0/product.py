class Product():

    def __init__(self, product_id: int, name: str, price: float):
        self.product_id = product_id
        self.name = name
        self.price = price
        pass


class LiquidProduct(Product):
    def __init__(self, product_id: int, name: str, price: float, volume: float):
        super().__init__(product_id, name, price)
        self.volume = volume



class SolidProduct(Product):
    def __init__(self, product_id: int, name: str, price: float, mass: float):
        super().__init__(product_id, name, price)
        self.mass = mass
