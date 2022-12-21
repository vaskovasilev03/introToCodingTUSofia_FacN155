from errors import InvalidCharacterClass
from .weapon import Weapon
class Character:
    CHARACTER_CLASSES = ("Warrior", "Mage", "Priest", "Rogue")
    def __init__(self, name, gender, rank) -> None:
        if rank not in Character.CHARACTER_CLASSES:
            raise InvalidCharacterClass("Class is invalid")
        self.name = name
        self.gender = gender
        self.rank = rank
        self.weapon = None
        self.secondaryitem = None

    def print(self):
        weapon_str = self.weapon.print() if self.weapon else "None"
        item_str = self.secondaryitem.print() if self.secondaryitem else "None"
        return f"Character({self.name}, {self.gender}, {self.rank}, {weapon_str}, {item_str})"

    def add_weapon(self, name, damage):
        if not self.weapon == None:
            self.weapon.name = name
            self.weapon.attack = damage
        else:
            self.weapon = Weapon(name, damage)
            print("Character Weapon Added")