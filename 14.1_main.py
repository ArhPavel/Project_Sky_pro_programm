from src.clases import Category, LawnGrass, Product, Smartphone

if __name__ == "__main__":
    # 1. Создание обычных продуктов
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    # 2. Создание объектов классов-наследников (Smartphone и LawnGrass)
    smartphone1 = Smartphone("iPhone 15 Pro", "512GB, Titanium", 150000.0, 3, 98.2, "15 Pro", 512, "Titanium")
    smartphone2 = Smartphone("Samsung S24", "256GB, Black", 110000.0, 5, 95.0, "S24", 256, "Black")

    grass1 = LawnGrass("Газон Премиум", "Универсальный", 500.0, 20, "Россия", 14, "Изумрудный")
    grass2 = LawnGrass("Газон Люкс", "Спортивный", 700.0, 10, "Германия", 10, "Темно-зеленый")

    # 3. Проверка строкового отображения (__str__)
    print("--- Строковое отображение товаров ---")
    print(str(product1))
    print(str(smartphone1))
    print(str(grass1))

    # 4. Проверка сложения товаров одного класса (__add__)
    print("\n--- Сложение товаров одного типа ---")
    print(f"Сумма стоимости остатков смартфонов: {smartphone1 + smartphone2} руб.")
    print(f"Сумма стоимости остатков газонной травы: {grass1 + grass2} руб.")

    # 5. Проверка запрета сложения товаров разных классов
    print("\n--- Проверка ограничений сложения ---")
    try:
        _ = smartphone1 + grass1
    except TypeError as e:
        print(f"Успешно перехвачена ошибка при сложении смартфона и травы: {e}")

    # 6. Создание категории и добавление продуктов
    category = Category("Смартфоны", "Современные мобильные телефоны", [smartphone1])
    print(f"\nКатегория до добавления: {category}")

    category.add_product(smartphone2)
    print(f"Категория после добавления смартфона: {category}")
    print("\nСписок товаров в категории:")
    print(category.products)

    # 7. Проверка запрета добавления некорректного объекта в категорию
    print("--- Проверка валидации добавления в категорию ---")
    try:
        category.add_product("Не продукт")
    except TypeError as e:
        print(f"Успешно перехвачена ошибка добавления постороннего объекта: {e}")
