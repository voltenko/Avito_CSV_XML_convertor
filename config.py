import os

# -----------------ПАРАМЕТРЫ СКРИПТА----------------

delimiter = ';'  # Разделитель колонок.

csv_encoding = 'windows-1251'  # Кодировка CSV файлов

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

csv_path = os.path.join(os.getcwd(), 'csv')  # Путь к папке с CSV
xml_path = os.path.join(os.getcwd(), 'xml')  # Путь к папке с XML

start_line = 0  # Строка, с которой начинаем читать CSV файл

# --------------------------------------------------
