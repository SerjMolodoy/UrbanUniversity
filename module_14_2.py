import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('not_telegram.db')
cursor = conn.cursor()

# Удаление записи с id = 6
cursor.execute('DELETE FROM Users WHERE id = 6')

# Подсчёт общего количества записей
cursor.execute('SELECT COUNT(*) FROM Users')
total_users = cursor.fetchone()[0]

# Подсчёт суммы всех балансов
cursor.execute('SELECT SUM(balance) FROM Users')
all_balances = cursor.fetchone()[0]

# Вычисление среднего баланса
average_balance = all_balances / total_users

# Вывод среднего баланса
print(average_balance)

# Закрытие соединения
conn.commit()
conn.close()