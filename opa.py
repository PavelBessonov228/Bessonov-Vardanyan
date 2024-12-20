import csv

# Открываем исходный CSV файл для чтения
file = open('fx_weekly_EUR_USD.csv', mode='r')
file_content = file.read()
    
    # Создаем словарь для хранения данных по каждому году
data_by_year = {}
for row in reader:
        year = int(row['Date'].split('-')[0])
        
        if year not in data_by_year:
            data_by_year[year] = {
                'max_open': float(row['Open']),
                'max_close': float(row['Close'])
            }
        else:
            data_by_year[year]['max_open'] = max(data_by_year[year]['max_open'], float(row['Open']))
            data_by_year[year]['max_close'] = max(data_by_year[year]['max_close'], float(row['Close']))

# Сортируем годы
sorted_years = sorted(data_by_year.keys())

# Открываем выходной TXT файл для записи результатов
with open('output.txt', 'w') as outfile:
    for year in sorted_years:
        outfile.write(f"{year}: Максимальная цена открытия {data_by_year[year]['max_open']}, максимальная цена закрытия {data_by_year[year]['max_close']}\n")
