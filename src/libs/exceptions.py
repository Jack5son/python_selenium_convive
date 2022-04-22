class ClassError(Exception):
    def __init__(self, message=None):
        self.message = message

        super().__init__(self.message)

    def __dict__(self):
        return {'message': self.message}


class Error(Exception):
    def __init__(self, message=None):
        self.message = message

        super().__init__(self.message)

    def __dict__(self):
        return {'message': self.message}