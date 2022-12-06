from random import randint
class MissingParameterError(Exception):
    pass

class InvalidParameterError(Exception):
    def __init__(self, invalid_parameter, *args):
        self.invalid_parameter = invalid_parameter
        self.message = f"Invalid class parameter: {invalid_parameter}"
        super().__init__(self.message, *args)

class InvalidAgeError(InvalidParameterError):
    pass

class InvalidSoundError(InvalidParameterError):
    pass


class JungleAnimal:
    def __init__(self, name="", age= 0, sound=""):
        # if not name or not age or not sound:
        #     raise MissingParameterError
        if type(name) != str:
            raise InvalidParameterError("name")
        elif type(age) != int:
            raise InvalidAgeError("age")
        elif type(sound) != str:
            raise InvalidSoundError("sound")
        self.name = name
        self.age = age
        self.sound = sound

    def __repr__(self): return 'JungleAnimal'

    def make_sound(self):
        print(f"{self.name} says {self.sound}!")

    def print(self):
        pass

    def daily_task(self):
        pass

class Jaguar(JungleAnimal):
    def __init__(self, name, age, sound):
        if age > 15:
            raise InvalidAgeError("age")
        elif len(sound) < 2:
            raise InvalidSoundError("sound")
        super().__init__(name, age, sound)

    def print(self):
        super().print()
        print(f"Jaguar({self.name}, {self.age}, {self.sound})")

    def __repr__(self): return 'Jaguar'

    def daily_task(self, animals):
        super().daily_task()
        for obj in animals:
            if not type(obj) == Jaguar:
                animal = animals.pop(animals.index(obj))
                print(f"{self.name} the Jaguar hunted down {obj.name} the {repr(animal)}")
                break

class Lemur(JungleAnimal):
    def __init__(self, name, age, sound):
        if age > 10:
            raise InvalidAgeError("age")
        elif 'e' not in sound:
            raise InvalidSoundError("sound")
        super().__init__(name, age, sound)

    def print(self):
        super().print()
        print(f"Lemur({self.name}, {self.age}, {self.sound})")

    def __repr__(self): return 'Lemur'

    def daily_task(self, fruitCount):
        if fruitCount >= 10:
            fruitCount -= 10
            print(f"{self.name} the Lemur ate a full meal of 10 fruits")
        elif fruitCount == 0:
            self.make_sound()
            self.make_sound()
            print(f"{self.name} the Lemur couldn't find anything to eat")
        elif fruitCount < 10:
            print(f"{self.name} the Lemur could only find {fruitCount} fruits")
        return f"Fruits left: {fruitCount}" 

class Human(JungleAnimal):
    def __init__(self, name, age, sound):
        if age > 10:
            raise InvalidAgeError("age")
        elif 'e' not in sound:
            raise InvalidSoundError("sound")
        super().__init__(name, age, sound)

    def print(self):
        super().print()
        print(f"Human({self.name}, {self.age}, {self.sound})")

    def __repr__(self): return 'Human'

    def daily_task(self, animals, buildings):
        i = animals.index(self)

        if i == 0 and type(animals[i + 1]) == Human:
            buildings.append(Building("Shelter"))
            print(f'{self.name} the Human build a Shelter')
        elif i == len(animals) - 1 and type(animals[i - 1]) == Human:
            buildings.append(Building("Shelter"))
            print(f'{self.name} the Human build a Shelter')
        elif type(animals[i + 1]) == Human and type(animals[i - 1]) == Human:
            buildings.append(Building("Shelter"))
            print(f'{self.name} the Human build a Shelter')
        
class Building:
    def __init__(self, type):
        self.type = type

fruits = 10
animals = []
buildings = []

names = [
    "Jacob",
    "David",
    "Bobby",
    "Steve",
    "Johanssen",
    "Mac",
    "Jason",
    "Edward",
    "Alex",
    "Maddie",
    "Susan",
    "Abigail",
    "Jessica",
    "Lizzy",
    "Monica",
    "Lorelei",
    "Sandra",
    "Michelle"
]

sounds = [
    "RAAWR",
    "ROAR",
    "Grrr",
    "Shriek",
    "Meow",
    "Eeek",
    "Aaaaa",
    "Speak",
    "I am a Human"
]


for i in range(102):
    random = randint(0, 9)
    ranAge = randint(0, 20)
    randNameIndex = randint(0, len(names)-1)
    randSoundIndex = randint(0, len(sounds)-1)

    try:
        if random < 4 and random >= 0:
            animals.append(Lemur(names[randNameIndex], ranAge, sounds[randSoundIndex]))
            print("A Lemur has entered the jungle")
        elif random > 3 and random < 8:
            animals.append(Jaguar(names[randNameIndex], ranAge, sounds[randSoundIndex]))
            print("A Jaguar has entered the jungle")
        elif random >= 8 and random < 10:
            animals.append(Human(names[randNameIndex], ranAge, sounds[randSoundIndex]))
            print("A Human has entered the jungle")

    except InvalidAgeError as e:
        print(f'{randNameIndex} {names[randNameIndex]} {randSoundIndex} {sounds[randSoundIndex]} {e}')

    except InvalidSoundError as e:
        print(f'{randNameIndex} {names[randNameIndex]} {randSoundIndex} {sounds[randSoundIndex]} {e}')

    except Exception as e:
        print(e)

print(f"The jungle now has {len(animals)} animals")

for anim in animals:
    if type(anim) == Lemur:
        print(anim.daily_task(fruits))
    elif type(anim) == Human:
        anim.daily_task(animals, buildings)
    elif type(anim) == Jaguar:
        anim.daily_task(animals)
    else:
        continue

print(f"The jungle now has {len(animals)} animals")
print(fruits)
print(animals)
print(buildings)
