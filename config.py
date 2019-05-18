import os

# -----------------ПАРАМЕТРЫ СКРИПТА----------------

delimiter = ';'  # Разделитель колонок.

csv_encoding = 'windows-1251'  # Кодировка CSV файлов

# Конфигурация соответствия номера колонки XML тэгу

columns_tags_map = {
    0: 'Id',
    7: 'Category',
    8: 'TypeId',
    9: 'AdType',
    1: 'ManagerName',
    2: 'ContactPhone',
    3: 'Region',
    4: 'City',
    5: 'Subway',
    6: 'Street',
    10: 'Title',
    11: 'Description',
    12: 'Price',
    13: 'Images'
}

csv_path = os.path.join(os.getcwd(), 'csv')  # Путь к папке с CSV
xml_path = os.path.join(os.getcwd(), 'xml')  # Путь к папке с XML

# --------------------------------------------------
