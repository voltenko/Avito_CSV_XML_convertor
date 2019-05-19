import config


def print_start_message():
    """Печатает стартовое сообщение с небольшой инструкциеей и информацией о параметрах приложения"""
    cells_str = '\n\t'.join([f'> {tag}' for tag in config.cells])

    start_message = f'''
        Привет! Сейчас я просканирую папку "csv" и попытаюсь конвертировать все найденные CSV, 
        удовлетворяющие требованиям, в XML для Avito. 

        Разделитель колонок - "{config.delimiter}".
        
        Файл должен содержать следующие колонки:
        {cells_str}
    '''
    print(start_message)

    input('Нажми "ENTER" чтобы продолжить')

    return True


