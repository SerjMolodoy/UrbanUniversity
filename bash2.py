import pandas as pd
import matplotlib.pyplot as plt

# Чтение данных из файла CSV
file_path = 'customers-1000.csv'
data = pd.read_csv(file_path)

# Вывод первых 5 строк для проверки данных
print(data.head())

# Пример 1: Гистограмма распределения клиентов по странам
plt.figure(figsize=(10, 6))
data['Country'].value_counts().plot(kind='bar', color='skyblue')
plt.title('Распределение клиентов по странам')
plt.xlabel('Страна')
plt.ylabel('Количество клиентов')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Пример 2: Круговая диаграмма распределения клиентов по городам (топ-10)
top_cities = data['City'].value_counts().head(10)
plt.figure(figsize=(8, 8))
plt.pie(top_cities, labels=top_cities.index, autopct='%1.1f%%', startangle=140)
plt.title('Топ-10 городов по количеству клиентов')
plt.show()

# Пример 3: Линейный график количества клиентов по дате подписки
data['Subscription Date'] = pd.to_datetime(data['Subscription Date'])
subscription_counts = data['Subscription Date'].dt.date.value_counts().sort_index()

plt.figure(figsize=(12, 6))
plt.plot(subscription_counts.index, subscription_counts.values, marker='o', linestyle='-', color='green')
plt.title('Количество клиентов по дате подписки')
plt.xlabel('Дата подписки')
plt.ylabel('Количество клиентов')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()