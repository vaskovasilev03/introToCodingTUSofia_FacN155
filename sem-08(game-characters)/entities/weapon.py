from errors import InvalidWeaponType
from .item import Item

class Weapon(Item):
    def __init__(self, name, attack) -> None:
        super().__init__(name)
        self.attack = attack

    def print(self):
        return f"Weapon({self.name}, {self.durability}, {self.attack})"