import os
import codecs
import csv
import config


def scan_csv_directory(path):
    """Получаем все CSV-файлы"""
    return [os.path.join(path, file) for file in os.listdir(path) if file.endswith('.csv')]


def open_all(file_names):
    """Открывакм все найденные файлы, создаем объекты"""
    csv_documents = []

    for file_name in file_names:
        with codecs.open(file_name, 'r', config.csv_encoding) as f_obj:
            csv_doc = list(csv.DictReader(f_obj, delimiter=config.delimiter))
            csv_documents.append(csv_doc)

    return csv_documents




