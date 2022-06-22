class Petrol:
    def __init__(self, quantity, location, petrol_type, petrol_price, discount):
        self.quantity = quantity
        self.location = location
        self.petrol_type = petrol_type
        self.petrol_price = petrol_price
        self.discount = discount

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity):
        self.__quantity = quantity

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location):
        self.__location = location

    @property
    def petrol_type(self):
        return self.__petrol_type

    @petrol_type.setter
    def petrol_type(self, petrol_type):
        self.__petrol_type = petrol_type

    @property
    def petrol_price(self):
        return self.__petrol_price

    @petrol_price.setter
    def petrol_price(self, petrol_price):
        self.__petrol_price = petrol_price

    @property
    def discount(self):
        return self.__discount

    @discount.setter
    def discount(self, discount):
        self.__discount = discount

    @property
    def purchase_amount(self):
        pms_cost = self.__petrol_price * self.__quantity
        return pms_cost

    @property
    def net_purchase(self):
        netPurch = self.__purchase_amount * self.__discount // 100
        return netPurch
