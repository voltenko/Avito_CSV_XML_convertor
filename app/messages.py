import config


def print_start_message():
    """Печатает стартовое сообщение с небольшой инструкциеей и информацией о параметрах приложения"""
    columns_tags_map_str = '\n\t'.join([f'{n} {tag}' for n, tag in config.columns_tags_map.items()])

    start_message = f'''
        Привет! Сейчас я просканирую папку "csv" и попытаюсь конвертировать все найденные CSV, 
        удовлетворяющие требованиям, в XML для Avito. 

        Разделитель колонок - "{config.separator}".
        
        Соответствие номера колонки (отсчёт с 0) XML тэгу:
        ---------------------------
        № | тэг
        ---------------------------
        {columns_tags_map_str}
        ---------------------------
    '''
    print(start_message)

    input('Нажми "ENTER" чтобы продолжить')

    return True


