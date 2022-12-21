class InvalidCommand(Exception):
    def __init__(self, message = "Command is invalid", *args: object) -> None:
        super().__init__(message, *args)

class InvalidDataFormat(Exception):
    pass

class CharacterExists(Exception):
    pass

class InvalidCharacterClass(Exception):
    pass

class InvalidCharacterData(Exception):
    pass

class InvalidGenderError(Exception):
    pass