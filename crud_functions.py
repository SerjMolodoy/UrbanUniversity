import sqlite3


# Функция для инициализации базы данных и создания таблицы Products
def initiate_db():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    # Создаем таблицу Products, если она еще не существует
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            price INTEGER NOT NULL
        )
    ''')

    conn.commit()
    conn.close()


# Функция для получения всех продуктов из таблицы Products
def get_all_products():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    # Получаем все записи из таблицы Products
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()

    conn.close()
    return products


# Функция для добавления продукта в таблицу Products
def add_product(title, description, price):
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    # Добавляем новую запись в таблицу Products
    cursor.execute('''
        INSERT INTO Products (title, description, price)
        VALUES (?, ?, ?)
    ''', (title, description, price))

    conn.commit()
    conn.close()