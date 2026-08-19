from typing import Any


class Product:
    """Класс продукта: имя, описание, цена и кол-во"""

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name: str = name
        self.description: str = description
        self.__price: float = price  # Приватный атрибут цены
        self.quantity: int = quantity

    @property
    def price(self) -> float:
        """Геттер для приватного атрибута цены"""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Сеттер для цены с проверкой на положительное значение"""
        if new_price > 0:
            self.__price = new_price
        else:
            print("Цена не должна быть нулевая или отрицательная")

    @classmethod
    def new_product(cls, product_data: dict[str, Any]) -> "Product":
        """Класс-метод для создания экземпляра Product из словаря"""
        # Превращаем Any | None в строго типизированные переменные, чтобы mypy не ругался
        name: str = str(product_data.get("name", ""))
        description: str = str(product_data.get("description", ""))
        price: float = float(product_data.get("price", 0.0))
        quantity: int = int(product_data.get("quantity", 0))

        return cls(name=name, description=description, price=price, quantity=quantity)


class Category:
    """Класс категории: имя, описание и список продуктов"""

    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: list[Product]) -> None:
        self.__name: str = name
        self.__description: str = description
        self.__products: list[Product] = products  # Приватный атрибут списка товаров

        Category.category_count += 1
        Category.product_count += len(self.__products)

    def add_product(self, product: Product) -> None:
        """Добавляет продукт в защищенный список и обновляет счетчик"""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Геттер возвращает строку со всеми продуктами строго по шаблону"""
        product_strings: list[str] = []
        for prod in self.__products:
            product_strings.append(f"{prod.name}, {prod.price} руб. Остаток: {prod.quantity} шт.\n")
        return "".join(product_strings)
