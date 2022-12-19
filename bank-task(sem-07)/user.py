from errors import UserAlreadyOwnsAccount
from errors import InvalidAccountData
class User:
    def __init__(self, names, egn) -> None:
        self.names = names
        self.egn = egn
        self.accounts = []

    def get_print(self):
        return f"User({self.names}, {self.egn}, accounts: [{len(self.accounts)}])"

    def add_account(self, account):
        if account in self.accounts:
            raise UserAlreadyOwnsAccount("Error: This account already belongs to this user")
        if len(account.iban) != 22 or len(account.currency) == "":
            raise InvalidAccountData("Error: Data is invalid")

        self.accounts.append(account)

    def get_accounts(self):
        for acc in self.accounts:
            print(acc.get_print(self.accounts))
        return self.accounts
