import sys
import config
import app.messages as messages
import app.csv_reader as csv_reader
import app.convertor as convertor
import app.exceptions


def main():
    """Точка входа"""
    messages.print_start_message()

    # получаем имена всех найденных CSV файлов
    csv_file_names = csv_reader.scan_csv_directory(config.csv_path)
    csv_docs = csv_reader.open_all(csv_file_names)

    for doc in csv_docs:
        try:
            doc.check()
        except app.exceptions.ValidationException as e:
            print(e.message)
            sys.exit(1)
        else:
            convertor.convert_csv_to_xml(doc)


if __name__ == '__main__':
    sys.exit(main())

