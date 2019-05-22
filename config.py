import os

# -----------------ПАРАМЕТРЫ СКРИПТА----------------

delimiter = ';'  # Разделитель колонок.
images_delimiter = ','  # Разделитель картинок.

csv_encoding = 'windows-1251'  # Кодировка CSV файлов
xml_encoding = 'utf-8'  # Кодировка XML файлов

# Список обязательных колонок

cells = [
    'Amount',
    'Length',
    'Id',
    'Category',
    'TypeId',
    'AdType',
    'ManagerName',
    'ContactPhone',
    'Region',
    'City',
    'Subway',
    'Street',
    'Title',
    'Description',
    'Price',
    'Images'
]

image_path = 'https://bmwday.ru/d/1902636/d/'

csv_path = os.path.join(os.getcwd(), 'csv')  # Путь к папке с CSV
xml_path = os.path.join(os.getcwd(), 'xml')  # Путь к папке с XML

start_line = 0  # Строка, с которой начинаем читать CSV файл

# --------------------------------------------------
