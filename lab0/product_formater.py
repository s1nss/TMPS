from product import Product, LiquidProduct


class ProductFormatter:
    @staticmethod
    def format_as_string(product: Product) -> str:
        return f"Product => {product.product_id}, {product.name}, Price: {product.price}"

    @staticmethod
    def format_as_json(product: Product) -> str:
        return f'{{"id": {product.product_id}, "name": "{product.name}", "price": {product.price}}}'

class LiquidProductFormater(ProductFormatter):
    @staticmethod
    def format_as_string(lproduct: LiquidProduct) -> str:
        return ProductFormatter.format_as_string(lproduct) + f"  Volume: {lproduct.volume}"