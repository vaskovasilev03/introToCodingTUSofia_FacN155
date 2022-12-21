from errors import InvalidCharacterClass
from .weapon import Weapon
from .item import Item

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
            change = input("Character already has a weapon.\nAre you sure you want to change the current weapon?\ny/n: ")
            if change == "y":
                self.weapon.name = name
                self.weapon.attack = damage
                print("New Character Weapon Saved")
            elif change == "n":
                print("Old Character Weapon Kept")
        else:
            self.weapon = Weapon(name, damage)
            print("Character Weapon Added")

    def add_item(self, name):
        if not self.secondaryitem == None:
            change = input("Character already has a secondary.\nAre you sure you want to change the current one?\ny/n: ")
            if change == "y":
                self.secondaryitem.name = name
                print("New Character Item Saved")
            elif change == "n":
                print("Old Character Item Kept")
        else:
            self.secondaryitem = Item(name)
            print("Character Secondary Item Added")