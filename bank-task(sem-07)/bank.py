from random import randint
from errors import UserNotFound, UserAlreadyExists, InvalidAmout, InvalidAccountIndex, InvalidCurrency, UnsufficientBalance
from account import Account
from user import User

class Bank:
    def __init__(self) -> None:
        self.users = []

    def find_user(self, user_egn: str) -> User:
        for u in self.users:
            if u.egn == user_egn:
                return u

    def add_user(self, names, egn):
        found_user = self.find_user(egn)

        if type(found_user) == User:
            raise UserAlreadyExists("User already exists")

        user = User(names, egn)
        self.users.append(user)

    def add_account(self, user_egn, currency, type):
        # user exists?
        found_user = self.find_user(user_egn)

        if found_user == None:
            raise UserNotFound("User does not exist")

        # generate iban
        iban = "BG9812"
        for i in range(0, 16):
            iban += str(randint(0, 9))

        # create account object
        account = Account(iban, currency, type)
        # call the user's add_account() methods
        found_user.add_account(account)
        print("Successfully added account:")
        print(f"New {type.capitalize()} Account >> IBAN({iban}, {currency}), Client: {found_user.names}\n")

    def user_accounts(self, user_egn: int) -> User:
        found_user = self.find_user(user_egn)

        if found_user == None:
            raise UserNotFound("User does not exist")

        return found_user.get_accounts()

    def deposit(self, user_egn):
        found_user = self.find_user(user_egn)

        if found_user == None:
            raise UserNotFound("User does not exist")

        for u in self.users:
            if u.egn == user_egn:
                print(self.user_accounts(u.egn))
                accIndex = input("Choose in which account you want to deposit (type the index of the account)> ")
                try:
                    if int(accIndex) + 1 > len(u.accounts):
                        raise InvalidAccountIndex("Error: Invalid Account Index")
                except ValueError:
                    raise InvalidAccountIndex("Error: Invalid Account Index")

                for i in range(len(u.accounts)):
                    if i == int(accIndex):
                        amount = input("Input amount you want to deposit: ")
                        curr = input("In what currency is your deposit? eur/bgn > ")
                        if type(curr) != str:
                            raise InvalidCurrency("Error: Invalid Currency")
                        try:
                            if u.accounts[i].currency == "EUR":
                                if curr.upper() == "EUR":
                                    u.accounts[i].balance += float(amount)
                                elif curr.upper() == "BGN":
                                    u.accounts[i].balance += float(amount)*0.51
                            elif u.accounts[i].currency == "BGN":
                                if curr.upper() == "EUR":
                                    u.accounts[i].balance += float(amount)*1.96
                                elif curr.upper() == "BGN":
                                    u.accounts[i].balance += float(amount)

                            print(f"Successful deposit, New Balance: [{u.accounts[i].balance} {u.accounts[i].currency}]")
                        except ValueError:
                            raise InvalidAmout("Error: Invalid Amount")
                
    def withdrawal(self, user_egn):
        found_user = self.find_user(user_egn)

        if found_user == None:
            raise UserNotFound("User does not exist")

        for u in self.users:
            if u.egn == user_egn:
                print(self.user_accounts(u.egn))
                accIndex = input("Choose from which account you want to withdraw (type the index of the account)> ")
                try:
                    if int(accIndex) + 1 > len(u.accounts):
                        raise InvalidAccountIndex("Error: Invalid Account Index")
                except ValueError:
                    raise InvalidAccountIndex("Error: Invalid Account Index")

                for i in range(len(u.accounts)):
                    if i == int(accIndex):
                        amount = input("Input amount you want to withdraw: ")

                        try:
                            if u.accounts[i].balance < float(amount):
                                raise UnsufficientBalance("Unsufficient Balance for operation")
                            else:
                                u.accounts[i].balance -= float(amount)
                                print(f"Successful withdraw, New Balance: [{u.accounts[i].balance} {u.accounts[i].currency}]")
                        except ValueError:
                            raise InvalidAmout("Error: Invalid Amount")
