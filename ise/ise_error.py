class InvalidFileFormatError(Exception):
    def __init__(self, message):
        self.message = message


class InvalidInstanceError(Exception):
    def __init__(self, message):
        self.message = message
