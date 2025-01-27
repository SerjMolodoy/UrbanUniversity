import requests
from bs4 import BeautifulSoup

# URL страницы с курсами валют
url = 'https://cbr.ru/currency_base/daily/'

# Заголовки для имитации запроса от браузера
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Выполнение GET-запроса
response = requests.get(url, headers=headers)

# Проверка статуса ответа
if response.status_code == 200:
    # Парсинг HTML-страницы
    soup = BeautifulSoup(response.text, 'html.parser')

    # Поиск таблицы с курсами валют
    table = soup.find('table', {'class': 'data'})

    if table:
        # Поиск всех строк таблицы
        rows = table.find_all('tr')

        # Вывод заголовков таблицы
        headers = [header.text.strip() for header in rows[0].find_all('th')]
        print(" | ".join(headers))

        # Вывод данных о валютах
        for row in rows[1:]:
            columns = row.find_all('td')
            if len(columns) == len(headers):
                data = [column.text.strip() for column in columns]
                print(" | ".join(data))
    else:
        print("Таблица с курсами валют не найдена.")
else:
    print(f"Ошибка: {response.status_code}")