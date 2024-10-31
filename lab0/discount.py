from product import Product

class Discount:
    def apply_discount(self, product: Product) -> float:
        pass

class PercentageDiscount(Discount):
    def __init__(self, percentage: float):
        self.percentage = percentage

    def apply_discount(self, product: Product) -> float:
        discount_amount = product.price * (self.percentage / 100)
        return product.price - discount_amount

class FixedDiscount(Discount):
    def __init__(self, amount: float):
        self.amount = amount

    def apply_discount(self, product: Product) -> float:
        return max(product.price - self.amount, 0)
