from typing import Any

import pytest

from src.clases import BaseProduct, Category, LawnGrass, Order, PrintMixin, Product, Smartphone


@pytest.fixture(autouse=True)
def reset_category_counters() -> None:
    """Фикстура автоматически сбрасывает счетчики перед каждым тестом."""
    Category.category_count = 0
    Category.product_count = 0


def test_base_product_cannot_be_instantiated() -> None:
    """Проверка, что нельзя создать экземпляр абстрактного класса BaseProduct."""
    with pytest.raises(TypeError):
        _ = BaseProduct("Имя", "Описание", 100.0, 1)  # type: ignore


def test_print_mixin_output(capsys: Any) -> None:
    """Тест работы миксина PrintMixin при создании продукта."""
    _ = Product("Samsung", "256GB", 180000.0, 5)
    captured = capsys.readouterr()
    assert "Product(" in captured.out
    assert "'Samsung'" in captured.out


def test_product_creation() -> None:
    """Тест создания объекта Product и работы геттера цены."""
    product = Product("Samsung", "256GB", 180000.0, 5)
    assert product.name == "Samsung"
    assert product.description == "256GB"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_product_str() -> None:
    """Тест строкового отображения продукта (__str__)."""
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет", 180000.0, 5)
    assert str(product) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_product_price_setter_valid() -> None:
    """Тест сеттера цены при положительном значении."""
    product = Product("Samsung", "256GB", 180000.0, 5)
    product.price = 200000.0
    assert product.price == 200000.0


def test_product_price_setter_invalid(capsys: Any) -> None:
    """Тест сеттера цены при отрицательном значении."""
    product = Product("Samsung", "256GB", 180000.0, 5)
    product.price = -500
    assert product.price == 180000.0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out


def test_new_product_classmethod() -> None:
    """Тест создания продукта через класс-метод new_product."""
    product_dict = {"name": "Xiaomi", "description": "64GB", "price": 20000.0, "quantity": 15}
    product = Product.new_product(product_dict)
    assert product.name == "Xiaomi"
    assert product.price == 20000.0
    assert product.quantity == 15


def test_category_counts_and_str() -> None:
    """Тест счетчиков и строкового отображения категории."""
    p1 = Product("Samsung", "256GB", 180000.0, 5)
    p2 = Product("Iphone", "128GB", 100000.0, 10)
    cat = Category("Смартфоны", "Связь", [p1, p2])

    assert Category.category_count == 1
    assert Category.product_count == 2
    assert str(cat) == "Смартфоны, количество продуктов: 15 шт."


def test_products_getter() -> None:
    """Тест геттера со списком продуктов."""
    p1 = Product("Samsung", "256GB", 180000.0, 5)
    cat = Category("Смартфоны", "Связь", [p1])
    assert cat.products == "Samsung, 180000.0 руб. Остаток: 5 шт.\n"


def test_smartphone_and_grass_creation() -> None:
    """Тест создания наследников Smartphone и LawnGrass."""
    phone = Smartphone("iPhone 15", "Флагман", 120000.0, 3, 98.5, "15 Pro", 256, "Titanium")
    grass = LawnGrass("Газон Премиум", "Универсальный", 500.0, 20, "Россия", 14, "Изумрудный")

    assert phone.model == "15 Pro"
    assert grass.country == "Россия"


def test_products_add_restrictions() -> None:
    """Тест сложения одинаковых классов и запрета разных."""
    p1 = Product("Товар 1", "Описание", 100.0, 10)
    p2 = Product("Товар 2", "Описание", 200.0, 2)
    assert p1 + p2 == 1400.0

    phone = Smartphone("iPhone", "Описание", 100000.0, 1, 95.0, "15", 256, "White")
    with pytest.raises(TypeError):
        _ = p1 + phone


def test_category_add_product_validation() -> None:
    """Тест валидации добавления продукта в категорию."""
    cat = Category("Разное", "Описание", [])
    product = Product("Товар", "Описание", 100.0, 5)
    cat.add_product(product)
    assert Category.product_count == 1

    with pytest.raises(TypeError):
        cat.add_product("Не продукт")


def test_order_creation_and_str() -> None:
    """Тест работы класса Заказ (Order)."""
    product = Product("Samsung", "256GB", 10000.0, 5)
    order = Order(product, 2)

    assert order.total_price == 20000.0
    assert "общая сумма: 20000.0 руб." in str(order)

    with pytest.raises(TypeError):
        _ = Order("Не продукт", 1)  # type: ignore


def test_print_mixin_custom_class(capsys: Any) -> None:
    """Тест работы PrintMixin на отдельном пользовательском классе."""

    class TestClass(PrintMixin):
        def __init__(self, value: int, text: str) -> None:
            self.value = value
            self.text = text
            super().__init__()

    _ = TestClass(42, "test")
    captured = capsys.readouterr()

    assert "TestClass(42, 'test')" in captured.out
