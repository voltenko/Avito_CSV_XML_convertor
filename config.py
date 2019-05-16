# -----------------ПАРАМЕТРЫ СКРИПТА----------------

delimiter = ';'  # Разделитель колонок.

# Конфигурация соответствия номера колонки XML тэгу

columns_tags_map = {
    0: 'Id',
    7: 'Category',
    8: 'TypeId',
    9: 'AdType',
    100: 'DateBegin',
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

# XML шаблон

XML_template = '''
<?xml version="1.0" encoding="utf-8"?>
<Ads formatVersion="3" target="Avito.ru">
    {body}
</ads>    
'''
# --------------------------------------------------
