class CreateBookException(Exception):
    def __init__(self, message='Не удалось создать книгу'):
        self.message = message
        super().__init__(self.message)
