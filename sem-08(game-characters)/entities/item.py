
class Item:

    def __init__(self, name) -> None:
        self.name = name
        self.durability = 100

    def print(self):
        return f"Item({self.name}, {self.durability})"