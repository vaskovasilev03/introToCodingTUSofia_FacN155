from entities import *
from errors import CharacterNotFound, InvalidCommand, CharacterExists, InvalidCharacterData, InvalidGenderError

class Menu:
    characters = []
    def print_menu(self):
        print("1. Create a new character")
        print("2. Add weapon to a character")
        print("3. Add item to a character")
        print("4. List all character")
        print("5. Exit")

    def exists(self, character):
        for ch in self.characters:
            if ch.name == character:
                return True
        return False

    def command_create_character(self, name, sex, ch_class):
        if type(name) != str:
            raise InvalidCharacterData("Name must be String")
        if len(name) < 4:
            raise InvalidCharacterData("Name must be 5 or more characters long")
        if not ch_class.isalpha():
            raise InvalidCharacterData("Class must be string input")
        newcharacter = Character(name, sex, ch_class)
        self.characters.append(newcharacter)
        print("Successfully Added New Character")

    def run(self):
        # infinite menu loop
        while True:  
            self.print_menu()
            choice = input("Choose an item from the menu: \n> ")
            
            try:
                if choice == "1":                    
                    name = input("Enter the character name (alpha-numeric): ")
                    if self.exists(name):
                        raise CharacterExists("Name is taken")
                    sex = input("Enter characters sex (male/female)? ")
                    if sex.isalpha():
                        if not sex == "male" and not sex == "female":
                            raise InvalidGenderError("Gender must be male or female")
                    else: 
                        raise InvalidGenderError("Gender be alpha-only")

                    ch_class = input("Enter character class:\n(Warrior, Mage, Priest or Rogue)/case insensitve/: ").lower().capitalize()
                    self.command_create_character(name, sex, ch_class)

                elif choice == "2":
                    ch_name = input("Enter characters name: ")
                    if not self.exists(ch_name):
                        raise CharacterNotFound("Character does not exist")
                    weapon = input("Enter Weapon Name: ")
                    attack = input("Enter Weapon Damage: ")
                    for k in Menu.characters:
                        if k.name == ch_name:
                            k.add_weapon(weapon, attack)

                elif choice == "3":
                    ch_name = input("Enter characters name: ")
                    if not self.exists(ch_name):
                        raise CharacterNotFound("Character does not exist")
                    item = input("Enter Item Name: ")
                    for k in self.characters:
                        if k.name == ch_name:
                            k.add_item(item)

                elif choice == "4":
                    i = 1
                    for ch in self.characters:
                        print(i, "-->", ch.print())
                        i += 1

                elif choice == "5":
                    print("See you!")
                    break
                else:
                    raise InvalidCommand("Error: Invalid choice")
            except Exception as ex:
                print(f"Error: {str(ex)}")
            
            print()

if __name__ == '__main__':
    menu = Menu()
    menu.run()