# inventory.py

from product import Product
from discount import Discount

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product: Product):
        self.products.append(product)

    def apply_discount(self, product_id: int, discount: Discount):
        product = next((p for p in self.products if p.product_id == product_id), None)
        if product:
            discounted_price = discount.apply_discount(product)
            print(f"Discounted price for {product.name}: ${discounted_price:.2f}")
        else:
            print("Product not found.")
