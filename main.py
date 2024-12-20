import functions

# URL страницы с Википедии
url = "https://en.wikipedia.org/wiki/ISO_4217"

try:
    # Получение HTML-кода страницы
    soup = functions.fetch_data_from_wikipedia(url)
    
    # Извлечение данных из таблицы
    data = functions.extract_currency_table(soup)
    
    # Создание DataFrame
    df = functions.create_dataframe(data)
    
    # Вывод DataFrame
    print(df)
except Exception as e:
    print(e)
