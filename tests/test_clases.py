from typing import Any

import pytest

from src.clases import Category, Product


@pytest.fixture(autouse=True)
def reset_category_counters() -> None:
    """Фикстура автоматически сбрасывает счетчики перед каждым тестом"""
    Category.category_count = 0
    Category.product_count = 0


def test_product_creation() -> None:
    """Тест создания объекта Product и работы геттера цены"""
    product = Product("Samsung", "256GB", 180000.0, 5)

    assert product.name == "Samsung"
    assert product.description == "256GB"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_product_str() -> None:
    """Тест строкового отображения продукта (__str__)"""
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет", 180000.0, 5)
    assert str(product) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_product_price_setter_valid() -> None:
    """Тест сеттера цены при передаче положительного значения"""
    product = Product("Samsung", "256GB", 180000.0, 5)
    product.price = 200000.0
    assert product.price == 200000.0


def test_product_price_setter_invalid(capsys: Any) -> None:
    """Тест сеттера цены при отрицательном или нулевом значении"""
    product = Product("Samsung", "256GB", 180000.0, 5)

    # Проверяем нулевую цену
    product.price = 0
    assert product.price == 180000.0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out

    # Проверяем отрицательную цену
    product.price = -500
    assert product.price == 180000.0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out


def test_new_product_classmethod() -> None:
    """Тест создания продукта через класс-метод new_product из словаря"""
    product_dict = {"name": "Xiaomi", "description": "64GB", "price": 20000.0, "quantity": 15}
    product = Product.new_product(product_dict)

    assert isinstance(product, Product)
    assert product.name == "Xiaomi"
    assert product.price == 20000.0
    assert product.quantity == 15


def test_category_counts() -> None:
    """Тест правильного подсчета количества категорий и продуктов при инициализации"""
    assert Category.category_count == 0
    assert Category.product_count == 0

    p1 = Product("Iphone", "128GB", 100000.0, 10)
    p2 = Product("Xiaomi", "64GB", 20000.0, 5)
    p3 = Product("TV", "4K", 50000.0, 2)

    Category("Смартфоны", "Связь", [p1, p2])
    assert Category.category_count == 1
    assert Category.product_count == 2

    Category("Телевизоры", "ТВ", [p3])
    assert Category.category_count == 2
    assert Category.product_count == 3


def test_category_str() -> None:
    """Тест строкового отображения категории (__str__) с подсчетом общего остатка на складе"""
    p1 = Product("Samsung", "256GB", 180000.0, 5)
    p2 = Product("Iphone", "128GB", 100000.0, 10)
    cat = Category("Смартфоны", "Связь", [p1, p2])

    # 5 + 10 = 15 шт.
    assert str(cat) == "Смартфоны, количество продуктов: 15 шт."


def test_add_product_and_counter() -> None:
    """Тест метода add_product и увеличения счетчика продуктов"""
    p1 = Product("Iphone", "128GB", 100000.0, 10)
    cat = Category("Смартфоны", "Связь", [p1])

    assert Category.product_count == 1

    p2 = Product("Xiaomi", "64GB", 20000.0, 5)
    cat.add_product(p2)

    assert Category.product_count == 2


def test_products_getter_string_format() -> None:
    """Тест геттера products на строгое соответствие шаблону строки"""
    p1 = Product("Samsung", "256GB", 180000.0, 5)
    p2 = Product("Iphone", "128GB", 100000.0, 10)
    cat = Category("Смартфоны", "Связь", [p1, p2])

    expected_output = "Samsung, 180000.0 руб. Остаток: 5 шт.\n" "Iphone, 100000.0 руб. Остаток: 10 шт.\n"

    assert cat.products == expected_output


def test_product_add_success() -> None:
    """Тест сложения двух продуктов: общая стоимость остатков"""
    p1 = Product("Товар A", "Описание", 100.0, 10)  # 100 * 10 = 1000
    p2 = Product("Товар B", "Описание", 200.0, 2)  # 200 * 2 = 400

    assert p1 + p2 == 1400.0


def test_product_add_invalid_type() -> None:
    """Тест вызова ошибки TypeError при сложении Product с другим типом"""
    p1 = Product("Товар A", "Описание", 100.0, 10)

    with pytest.raises(TypeError):
        _ = p1 + 500
