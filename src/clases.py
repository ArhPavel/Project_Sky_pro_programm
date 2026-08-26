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
        name: str = str(product_data.get("name", ""))
        description: str = str(product_data.get("description", ""))
        price: float = float(product_data.get("price", 0.0))
        quantity: int = int(product_data.get("quantity", 0))

        return cls(name=name, description=description, price=price, quantity=quantity)

    def __str__(self) -> str:
        """Строковое отображение: Название продукта, 80 руб. Остаток: 15 шт."""
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: Any) -> float:
        """Сложение двух продуктов: возвращает суммарную стоимость их остатков на складе"""
        if type(other) is not Product and not isinstance(other, Product):
            raise TypeError("Складывать можно только объекты класса Product")
        return (self.price * self.quantity) + (other.price * other.quantity)


class Category:
    """Класс категории: имя, описание и список продуктов"""

    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: list[Product]) -> None:
        self.__name: str = name  # Приватный атрибут
        self.__description: str = description  # Приватный атрибут
        self.__products: list[Product] = products  # Приватный список товаров

        Category.category_count += 1
        Category.product_count += len(self.__products)

    @property
    def name(self) -> str:
        """Геттер для приватного имени категории"""
        return self.__name

    @property
    def description(self) -> str:
        """Геттер для приватного описания категории"""
        return self.__description

    def add_product(self, product: Product) -> None:
        """Добавляет продукт в приватный список и обновляет счетчик"""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Геттер возвращает строку со всеми продуктами через __str__"""
        product_strings: list[str] = [f"{str(prod)}\n" for prod in self.__products]
        return "".join(product_strings)

    def __str__(self) -> str:
        """Строковое отображение: Название категории, количество продуктов: 200 шт."""
        total_quantity: int = sum(prod.quantity for prod in self.__products)
        return f"{self.__name}, количество продуктов: {total_quantity} шт."
