import requests
from bs4 import BeautifulSoup
import pandas as pd

def fetch_data_from_wikipedia(url):
    """
    Функция для получения HTML-кода страницы с Википедии.
    :param url: URL страницы Википедии.
    :return: объект BeautifulSoup.
    """
    response = requests.get(url)
    if response.status_code == 200:
        return BeautifulSoup(response.text, 'html.parser')
    else:
        raise Exception(f"Ошибка запроса: {response.status_code}")

