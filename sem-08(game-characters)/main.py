from entities import Character
from errors import InvalidCommand, CharacterExists, InvalidCharacterData, InvalidGenderError

class Menu:
    characters = []
    def print_menu(self):
        print("1. Create a new character")
        print("2. Add weapon to a character")
        print("3. Add item to a character")
        print("4. List all character")
        print("5. Exit")

    def command_create_character(self, name, sex, ch_class):
        if len(name) < 4:
            raise InvalidCharacterData("Name must be 5 or more characters long")
        if not ch_class.isalpha():
            raise InvalidCharacterData("Class must be string input")
        if name in Menu.characters:
            raise CharacterExists("Error: Character already exists")
        newcharacter = Character(name, sex, ch_class)
        Menu.characters.append(newcharacter)

    def run(self):
        # infinite menu loop
        while True:  
            self.print_menu()
            choice = input("Choose an item from the menu: \n> ")
            # catch errors
            try:
                # process the user's choice
                if choice == "1":                    
                    # ask the user to input the necessary command parameters
                    name = input("Enter the character name (alpha-numeric): ")
                    sex = input("Enter characters sex (male/female)? ")
                    if sex.isalpha():
                        if not sex == "male" and not sex == "female":
                            raise InvalidGenderError("Gender must be male or female")
                    else: 
                        raise InvalidGenderError("Gender be alpha-only")

                    ch_class = input("Enter Character Class(Mage, ...): ")

                    self.command_create_character(name, sex, ch_class)

                elif choice == "2":
                    ch_name = input("Enter characters name: ")
                    weapon = input("Enter weapon name: ")
                    attack = input("Enter Weapon Damage")
                    
                else:
                    raise InvalidCommand("Error: Invalid choice")
            except Exception as ex:
                print(f"Error: {str(ex)}")
            
            print()

if __name__ == '__main__':
    menu = Menu()
    menu.run()