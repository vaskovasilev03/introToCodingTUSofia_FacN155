class MissingParameterError(Exception):
    pass

class InvalidParameterError(Exception):
    def __init__(self, invalid_parameter, *args):
        self.invalid_parameter = invalid_parameter
        message = f"Invalid Parameter: {invalid_parameter}"
        super().__init__(message, *args)

class InvalidAgeError(InvalidParameterError):
    pass

class InvalidSoundError(InvalidParameterError):
    pass

class JungleAnimal:
    def __init__(self, name, age, sound):
        if type(name) != str:
            raise InvalidParameterError(f"{name}")
        elif type(age) != int:
            raise InvalidAgeError("Invalid Age!")
        elif type(sound) != str:
            raise InvalidSoundError("Invalid Sound!")
        self.name = name
        self.age = age
        self.sound = sound
    
    def make_sound(self):
        print(f"{self.name} says {self.sound}!")

    def print(self):
        pass

    def daily_task(self):
        pass

class Jaguar(JungleAnimal):
    def __init__(self, name, age, sound):
        if age > 15:
            raise InvalidAgeError
        elif len(sound) < 2:
            raise InvalidSoundError
        super().__init__(name, age, sound)

    def print(self):
        super().print()
        print(f"Jaguar({self.name}, {self.age}, {self.sound})")

    def daily_task(self, animals):
        for obj in animals:
            if type(obj) == Lemur or type(obj) == Human:
                del obj
        super().daily_task()
        print(f"{self.name} the Jaguar hunted down {self.animal.name} the {self.animal_class.__name__}")

class Lemur(JungleAnimal):
    def __init__(self, name, age, sound):
        if age > 10:
            raise InvalidAgeError
        elif 'e' not in sound:
            raise InvalidSoundError
        super().__init__(name, age, sound)
