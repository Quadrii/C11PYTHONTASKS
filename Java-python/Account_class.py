class Account:
    def __init__(self, name, balance: int):
        self._name = name
        self._balance = balance

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, balance):
        if balance > 0:
            self._balance = balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Amount cannot be less than 0")
        else:
            self._balance = self._balance + amount
