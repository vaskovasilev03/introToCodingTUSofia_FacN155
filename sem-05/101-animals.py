from random import randint
class MissingParameterError(Exception):
    pass

class InvalidParameterError(Exception):
    def __init__(self, invalid_parameter):
        self.invalid_parameter = invalid_parameter
        message = f"Invalid class parameter: {invalid_parameter}"
        super().__init__(message)

class InvalidAgeError(InvalidParameterError):
    def __init__(self):
        invalid_parameter = "age"
        super().__init__(invalid_parameter)

class InvalidSoundError(InvalidParameterError):
    def __init__(self):
        invalid_parameter = "sound"
        super().__init__(invalid_parameter)


class JungleAnimal:
    def __init__(self, name="", age= 0, sound=""):
        if not name or not age or not sound:
            raise MissingParameterError()
        if type(name) != str:
            raise InvalidParameterError("name")
        elif type(age) != int:
            raise InvalidAgeError()
        elif type(sound) != str:
            raise InvalidSoundError()
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
        super().__init__(name, age, sound)
        if age > 15:
            raise InvalidAgeError()
        elif sound.lower().count('r') < 2:
            raise InvalidSoundError()
        

    def print(self):
        super().print()
        print(f"Jaguar({self.name}, {self.age}, {self.sound})")

    def __repr__(self): return f'Jaguar({self.name})'

    def daily_task(self, animals):
        super().daily_task()
        for i in range(len(animals)):
            if type(animals[i]) == Human or type(animals[i]) == Lemur:
                print(f'{self.name} the Jaguar hunted down {animals[i].name} the {repr(animals[i])}')
                del animals[i]
                break

    # def daily_task(self, animals):
    #     super().daily_task()
    #     for obj in animals:
    #         if not type(obj) == Jaguar:
    #             animal = animals.pop(animals.index(obj))
    #             print(f"{self.name} the Jaguar hunted down {obj.name} the {repr(animal)}")
    #             break

class Lemur(JungleAnimal):
    def __init__(self, name, age, sound):
        super().__init__(name, age, sound)
        if age > 10:
            raise InvalidAgeError()
        elif 'e' not in sound:
            raise InvalidSoundError()

    def print(self):
        super().print()
        print(f"Lemur({self.name}, {self.age}, {self.sound})")

    def __repr__(self): return f'Lemur({self.name})'

    def daily_task(self, fruitCount):
        if fruitCount >= 10:
            fruitCount -= 10
            print(f"{self.name} the Lemur ate a full meal of 10 fruits")
        elif fruitCount > 0:
            print(f"{self.name} the Lemur could only find {fruitCount} fruits")
            fruitCount -= fruitCount
        else:
            self.make_sound()
            self.make_sound()
            print(f"{self.name} the Lemur couldn't find anything to eat")
        return f"Fruits: {fruitCount}"

class Human(JungleAnimal):
    def __init__(self, name, age, sound):
        super().__init__(name, age, sound)
        if age < 10:
            raise InvalidAgeError()
        elif 'a' not in sound:
            raise InvalidSoundError()

    def print(self):
        super().print()
        print(f"Human({self.name}, {self.age}, {self.sound})")

    def __repr__(self): return f'Human({self.name})'

    def daily_task(self, animals, buildings, types):
        i = animals.index(self)

        randBuildType = randint(0, len(types)-1)
        building = types[randBuildType]

        if i == 0:
            if type(animals[i + 1]) == Human:
                buildings.append(Building(building, self.name))
                print(f'{self.name} the Human build a {building}')
        elif i == len(animals) - 1:
            if type(animals[i - 1]) == Human:
                buildings.append(Building(building, self.name))
                print(f'{self.name} the Human build a {building}')
        else:
            if type(animals[i - 1]) == Human and type(animals[i + 1]) == Human:
                buildings.append(Building(building, self.name))
                print(f'{self.name} the Human build a {building}')

        
class Building:
    def __init__(self, type, owner):
        self.type = type
        self.owner = owner
    
    def __repr__(self):
        return f"{self.type}(Owner: {self.owner})"

fruits = 6
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

buildingTypes = [
    "Hut",
    "Shelter",
    "Tent",
    "Campfire Place",
    "Tree House"
]

for i in range(102):
    random = randint(0, 9)
    ranAge = randint(7, 20)
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
        anim.daily_task(animals, buildings, buildingTypes)
    elif type(anim) == Jaguar:
        anim.daily_task(animals)
    else:
        continue

print(f"The jungle now has {len(animals)} animals")
print(fruits)
print(animals)
print(buildings)
