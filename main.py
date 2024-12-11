import requests
from bs4 import BeautifulSoup
import pandas as pd
# URL страницы с Википедии
url = "https://en.wikipedia.org/wiki/ISO_4217"

# Отправка GET-запроса
response = requests.get(url)

# Проверка статуса запроса
if response.status_code == 200:
    # Создание объекта BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Поиск таблицы с данными о валютах
    table = soup.find("table", {"class": "wikitable sortable"})
    
    # Проверка наличия таблицы
    if table:
        rows = table.find_all("tr")
        data = []
        
        # Обработка строк таблицы
        for row in rows[1:]:  # Пропускаем заголовок таблицы
            cols = row.find_all("td")
            if len(cols) >= 3:  # Убедимся, что есть все нужные данные
                code = cols[0].text.strip()
                num = cols[1].text.strip()
                currency = cols[2].text.strip()
                data.append([code, num, currency])