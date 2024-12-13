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
        
        # Создание DataFrame для структурирования данных
        df = pd.DataFrame(data, columns=["Code", "Num", "Currency"])
        print(df)
    else:
        print("Таблица с данными о валютах не найдена.")
else:
    print(f"Ошибка запроса: {response.status_code}")