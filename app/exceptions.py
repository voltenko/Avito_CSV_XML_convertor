class ValidationException(Exception):
    """Ошибка валидации CSV файла"""
    def __init__(self, message):
        Exception.__init__(self)
        self.message = message

