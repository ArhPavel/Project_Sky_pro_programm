from abc import ABC, abstractmethod
from typing import Any


class PrintMixin:
    """Миксин, который печатает в консоль информацию о создании объекта."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        print(repr(self))

    def __repr__(self) -> str:
        # Автоматически собирает имя класса и переданные в экземпляр атрибуты
        attrs = ", ".join(f"{repr(v)}" for v in self.__dict__.values())
        return f"{self.__class__.__name__}({attrs})"


class BaseProduct(ABC):
    """Базовый абстрактный класс для всех продуктов."""

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name: str = name
        self.description: str = description
        self._price: float = price
        self.quantity: int = quantity

    @property
    @abstractmethod
    def price(self) -> float:
        """Геттер цены обязателен для каждого продукта."""
        pass

    @price.setter
    @abstractmethod
    def price(self, new_price: float) -> None:
        """Сеттер цены обязателен для каждого продукта."""
        pass

    @abstractmethod
    def __str__(self) -> str:
        """Строковое отображение обязательно для каждого продукта."""
        pass

    @abstractmethod
    def __add__(self, other: Any) -> float:
        """Сложение обязательно для каждого продукта."""
        pass


class Product(PrintMixin, BaseProduct):
    """Класс продукта: имя, описание, цена и количество."""

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        super().__init__(name=name, description=description, price=price, quantity=quantity)

    @property
    def price(self) -> float:
        """Геттер для цены."""
        return self._price

    @price.setter
    def price(self, new_price: float) -> None:
        """Сеттер для цены с валидацией."""
        if new_price > 0:
            self._price = new_price
        else:
            print("Цена не должна быть нулевая или отрицательная")

    @classmethod
    def new_product(cls, product_data: dict[str, Any]) -> "Product":
        """Класс-метод для создания экземпляра Product из словаря."""
        name: str = str(product_data.get("name", ""))
        description: str = str(product_data.get("description", ""))
        price: float = float(product_data.get("price", 0.0))
        quantity: int = int(product_data.get("quantity", 0))

        return cls(name=name, description=description, price=price, quantity=quantity)

    def __str__(self) -> str:
        """Строковое отображение: Название продукта, 80 руб. Остаток: 15 шт."""
        return f"{self.name}, {self._price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: Any) -> float:
        """Сложение стоимости всех товаров строго одинаковых классов."""
        if type(self) is not type(other):
            raise TypeError("Складывать можно только товары одного и того же класса")
        return (self.price * self.quantity) + (other.price * other.quantity)


class Smartphone(Product):
    """Класс смартфона, наследуется от Product."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
        super().__init__(name, description, price, quantity)


class LawnGrass(Product):
    """Класс газонной травы, наследуется от Product."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: int,
        color: str,
    ) -> None:
        self.country = country
        self.germination_period = germination_period
        self.color = color
        super().__init__(name, description, price, quantity)


class BaseOrderCategory(ABC):
    """Абстрактный класс для сущностей, содержащих продукты (Категория, Заказ)."""

    @abstractmethod
    def __str__(self) -> str:
        """Строковое представление сущности."""
        pass


class Category(BaseOrderCategory):
    """Класс категории: имя, описание и список продуктов."""

    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: list[Any]) -> None:
        self.__name: str = name
        self.__description: str = description
        self.__products: list[BaseProduct] = list(products)  # Аннотируем как BaseProduct

        Category.category_count += 1
        Category.product_count += len(self.__products)

    @property
    def name(self) -> str:
        """Геттер для названия категории."""
        return self.__name

    @property
    def description(self) -> str:
        """Геттер для описания категории."""
        return self.__description

    def add_product(self, product: Any) -> None:
        """Добавляет продукт в категорию с валидацией типа."""
        if not isinstance(product, BaseProduct):
            raise TypeError("Можно добавлять только объекты класса Product или его наследников")
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Геттер возвращает строку со всеми продуктами."""
        product_strings: list[str] = [f"{str(prod)}\n" for prod in self.__products]
        return "".join(product_strings)

    def __str__(self) -> str:
        """Строковое отображение категории."""
        total_quantity: int = sum(prod.quantity for prod in self.__products)
        return f"{self.__name}, количество продуктов: {total_quantity} шт."


class Order(BaseOrderCategory):
    """Класс Заказа на покупку одного конкретного товара."""

    def __init__(self, product: Product, quantity: int) -> None:
        if not isinstance(product, BaseProduct):
            raise TypeError("В заказ можно передать только объект продукта")
        self.product: Product = product
        self.quantity: int = quantity
        self.total_price: float = product.price * quantity

    def __str__(self) -> str:
        """Строковое отображение заказа."""
        return f"Заказ: {self.product.name}, {self.quantity} шт., общая сумма: {self.total_price} руб."
