from src.clases import Category, LawnGrass, Order, Product, Smartphone

if __name__ == "__main__":
    print("--- 1. Создание объектов (проверка работы PrintMixin) ---")
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый", 180000.0, 5)
    phone = Smartphone("iPhone 15 Pro", "512GB", 150000.0, 3, 98.2, "15 Pro", 512, "Titanium")
    grass = LawnGrass("Газон Премиум", "Универсальный", 500.0, 20, "Россия", 14, "Зеленый")

    print("\n--- 2. Проверка работы строкового отображения ---")
    print(product)
    print(phone)
    print(grass)

    print("\n--- 3. Проверка сложения ---")
    product2 = Product("Xiaomi Redmi Note 11", "1024GB", 31000.0, 14)
    print(f"Сумма запасов Product: {product + product2} руб.")

    try:
        _ = phone + grass
    except TypeError as e:
        print(f"Ограничение сложения сработало: {e}")

    print("\n--- 4. Проверка категории и добавления продуктов ---")
    category = Category("Смартфоны", "Категория смартфонов", [phone])
    print(category)

    print("\n--- 5. Проверка оформления Заказа (Order) ---")
    order = Order(product, 3)
    print(order)
