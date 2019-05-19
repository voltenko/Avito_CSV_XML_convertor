import os
import codecs
import csv
import config
import app.exceptions as exceptions


def scan_csv_directory(path):
    """Получаем все CSV-файлы"""
    return [os.path.join(path, file) for file in os.listdir(path) if file.endswith('.csv')]


def open_all(file_names):
    """Открывакм все найденные файлы, создаем объекты"""
    csv_documents = []

    for file_name in file_names:
        with codecs.open(file_name, 'r', config.csv_encoding) as f_obj:
            csv_doc = CsvDocument(list(csv.DictReader(f_obj, delimiter=config.delimiter)), file_name)
            csv_documents.append(csv_doc)

    return csv_documents


class CsvDocument:
    """CSV- документ, полученный из файла"""
    def __init__(self, data, name):
        self.data = data
        self.name = name

    def check(self):
        """Проверяем CSV-шник"""
        # Множество для проверки уникальности айдишников
        ids = set()
        for index, line in enumerate(self.data[config.start_line:]):

            for cell in config.cells:
                # Проверяем, что в файле есть все колонки
                if cell not in line:
                    raise exceptions.ValidationException(
                        f'Ошибка! Отсутствует колонка {cell}. Файл: {self.name}, строка: {index}'
                    )

                # Проверяем, что все ячейки заполнены
                if line[cell] == '':
                    raise exceptions.ValidationException(
                        f'Ошибка! Пустая ячейка {cell}. Файл: {self.name}, строка: {index}'
                    )

            # Если количекство 0, то удаляем строку
            if int(line['Amount']) == 0:
                del self.data[index]
                continue

            # Проверяем, что длина меньше 50
            if int(line['Length']) > 50:
                raise exceptions.ValidationException(f'Ошибка! Длина больше 50. Файл: {self.name}, строка: {index}')

            # Проверяем уникальность айдишника
            if line['Id'] in ids:
                raise exceptions.ValidationException(f'Ошибка! id - {line["Id"]} повторяется. Файл: {self.name}, строка: {index}')
            else:
                ids.add(line['Id'])
