class Car:
    def __init__(self, type: str, year: int, price: float):
        self._type = type
        self._year = year
        self._price = price

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        self._type = type

    @property
    def year(self):
        return self._year

    @year.setter
    def type(self, year):
        self._year = year

    @property
    def price(self):
        return self._price

    @price.setter
    def type(self, price):
        if price < 0:
            raise ValueError("price should be greater than or equals to 0")
        self._price = price

    def calcDiscount(self, discount: float):
        discount_price = self._price - (discount * self._price)
        return discount_price
