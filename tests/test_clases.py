import pytest
from src.clases import Product, Category


# Фикстура, которая автоматически сбрасывает счетчики перед каждым тестом
@pytest.fixture(autouse=True)
def reset_category_counters():
    Category.category_count = 0
    Category.product_count = 0


def test_product_creation():
    """Тест успешного создания объекта Product и присвоения атрибутов"""
    product = Product("Samsung", "256GB", 180000.0, 5)

    assert product.name == "Samsung"
    assert product.description == "256GB"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_category_creation():
    """Тест успешного создания объекта Category"""
    product = Product("Samsung", "256GB", 180000.0, 5)
    category = Category("Смартфоны", "Телефоны", [product])

    assert category.name == "Смартфоны"
    assert category.description == "Телефоны"
    assert len(category.products) == 1
    assert category.products[0].name == "Samsung"


def test_category_counts():
    """Тест правильного подсчета количества категорий и продуктов"""
    assert Category.category_count == 0
    assert Category.product_count == 0

    p1 = Product("Iphone", "128GB", 100000.0, 10)
    p2 = Product("Xiaomi", "64GB", 20000.0, 5)
    p3 = Product("TV", "4K", 50000.0, 2)

    # Создаем первую категорию с 2 продуктами
    cat1 = Category("Смартфоны", "Связь", [p1, p2])

    assert Category.category_count == 1
    assert Category.product_count == 2

    # Создаем вторую категорию с 1 продуктом
    cat2 = Category("Телевизоры", "ТВ", [p3])

    assert Category.category_count == 2
    assert Category.product_count == 3