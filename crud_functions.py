import sqlite3


# Функция для инициализации базы данных и создания таблиц Products и Users
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

    # Создаем таблицу Users, если она еще не существует
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL,
            age INTEGER NOT NULL,
            balance INTEGER NOT NULL DEFAULT 1000
        )
    ''')

    conn.commit()
    conn.close()


# Функция для добавления пользователя в таблицу Users
def add_user(username, email, age):
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    # Добавляем новую запись в таблицу Users
    cursor.execute('''
        INSERT INTO Users (username, email, age, balance)
        VALUES (?, ?, ?, 1000)
    ''', (username, email, age))

    conn.commit()
    conn.close()


# Функция для проверки наличия пользователя в таблице Users
def is_included(username):
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    # Проверяем, есть ли пользователь с таким именем
    cursor.execute('SELECT * FROM Users WHERE username = ?', (username,))
    user = cursor.fetchone()

    conn.close()
    return user is not None  # Возвращаем True, если пользователь найден, иначе False


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
