import config

start_message = f'''
    Привет! Сейчас я просканирую текущую папку и попытаюсь конвертировать все найденные CSV, 
    удовлетворяющие требованиям, в XML для Avito. 

    Вот список требований для исходных CSV файлов: 

    Разделитель колонок - {config.delimiter}.
'''

print(start_message)