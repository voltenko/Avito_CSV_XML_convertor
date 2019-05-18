import sys
import config
import app.messages as messages
import app.csv_reader as csv_reader


def main():
    """Точка входа"""
    messages.print_start_message()

    # получаем имена всех найденных CSV файлов
    csv_file_names = csv_reader.scan_csv_directory(config.csv_path)
    csv_docs = csv_reader.open_all(csv_file_names)

    print(csv_docs)

if __name__ == '__main__':
    sys.exit(main())
