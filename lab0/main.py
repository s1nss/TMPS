# main.py

from product import LiquidProduct, SolidProduct, Product
from inventory import Inventory
from discount import PercentageDiscount, FixedDiscount
from product_formater import ProductFormatter, LiquidProductFormater

inventory = Inventory()
p_formater = ProductFormatter
lp_formater = LiquidProductFormater

p1 = LiquidProduct(1, "Laptop", 1200.0, 5)
p2 = SolidProduct(2, "Smartphone", 800.0, 10)

inventory.add_product(p1)
inventory.add_product(p2)

percentage_discount = PercentageDiscount(10)
fixed_discount = FixedDiscount(100)

inventory.apply_discount(1, percentage_discount)
inventory.apply_discount(2, fixed_discount)

print(lp_formater.format_as_string(p1))
print(p_formater.format_as_json(p1))
print(p_formater.format_as_string(p2))

