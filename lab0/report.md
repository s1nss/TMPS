# SOLID Principles

## Author: Vlad Pruteanu

----

## Objectives:
* To understand and apply the SOLID principles of object-oriented design
* To implement 2 SOLID principles in code

## Used Design Patterns:
* S - Single Responsibility Principle
* O - Open Closed Principle
* D - Dependency Inversion Principle


## Implementation

### Single Responsibility Principle
- **Product**: it is responding for holding product data and lets other classes do calculations, keeping only one job .

```python
class Product():

    def __init__(self, product_id: int, name: str, price: float):
        self.product_id = product_id
        self.name = name
        self.price = price
        pass

```

p.s even for printing the product there is an separate class

###  Open Closed Principle

- **Product**  is an class that is open for extensions via other subclasses and closed for modifications


```python
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


```

### Dependency Inversion Principle

- **Inventory** class instead of directly addressing `FixedDiscount` class, it depends on abstraction of this class


```python

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

```

## Conclusions / Screenshots / Results

This lab introduced key SOLID principles to design modular, maintainable code. By applying the Single Responsibility Principle, we ensured each class had a focused role, while the Open-Closed Principle enabled easy extension through subclassing without modifying existing structures. The Dependency Inversion Principle allowed for flexible dependency management, improving adaptability and simplifying potential future changes in functionality.

