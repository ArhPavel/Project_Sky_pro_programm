class Product:
    """Класс продукта: имя, описание, цена и кол-во"""
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

class Category:
    """Класс продукта: имя, описание, цена и кол-во"""
    name: str
    description: str
    product: list

    category_count = 0
    product_count = 0

    def __init__(self, name, description, product):
        self.name = name
        self.description = description
        self.products = product

        Category.category_count += 1

        Category.product_count += len(self.products)
