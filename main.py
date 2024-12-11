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