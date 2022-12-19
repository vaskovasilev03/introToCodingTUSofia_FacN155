from errors import InvalidAccountType, InvalidCurrency

class Account:
    ACC_TYPES = ("SAVINGS", "CREDIT")

    def __init__(self, iban, currency, type) -> None:
        if type not in Account.ACC_TYPES:
            raise InvalidAccountType("Account type is invalid")
        if currency != "EUR" and currency != "BGN":
            raise InvalidCurrency("Currency must be EUR or BGN")
        self.iban = iban
        self.currency = currency
        self.type = type
        self.balance = 0

    def get_print(self, useraccounts):
        index = useraccounts.index(self)
        return f"Account [{index}] -> (IBAN: {self.iban}, currency: {self.currency}, type: {self.type}) [Balance: {self.balance}]"