class Petrol:
    def __init__(self, quantity, location, petrol_type, petrol_price):
        self._quantity = quantity
        self._location = location
        self._petrol_type = petrol_type
        self._petrol_price = petrol_price

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        self._quantity = quantity

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, location):
        self._location = location

    @property
    def petrol_type(self):
        return self._petrol_type

    @petrol_type.setter
    def petrol_type(self, petrol_type):
        self._petrol_type = petrol_type

    @property
    def petrol_price(self):
        return self._petrol_price

    @petrol_price.setter
    def petrol_price(self, petrol_price):
        self._petrol_price = petrol_price

    def purchase_amount(self):
        pms_cost = self._petrol_price * self._quantity
        return pms_cost

    def net_purchase(self, discount):
        convertDiscount = discount / 100
        netPurch = Petrol.purchase_amount(self) - (Petrol.purchase_amount(self) * convertDiscount)
        return netPurch
