class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def car_description(self):
        return "The ", self.color, " car has", self.mileage, "miles"

    def drive(self, drived):
        return drived + self.mileage


blue_car = Car("blue", 15000)
print(blue_car.car_description())
red_car = Car("red", 18000)
print(red_car.car_description())
new_car = Car("white", 10000)
print(new_car.car_description())
print(new_car.drive(3000))
