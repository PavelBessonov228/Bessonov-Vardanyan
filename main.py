import requests
from bs4 import BeautifulSoup
import pandas as pd
# URL страницы с Википедии
url = "https://en.wikipedia.org/wiki/ISO_4217"

# Отправка GET-запроса
response = requests.get(url)

# Проверка статуса запроса
if response.status_code == 200: