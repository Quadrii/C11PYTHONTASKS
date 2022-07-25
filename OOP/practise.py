class Persons:
    def __init__(self, name: str) -> None:
        self._Persons__name = None
        self.__name = name
        self.__age = 27

    @property
    def Persons__name(self):
        return self._Persons__name


person1 = Persons("Abigail")
print(person1.Persons__name)


class Person:
    def __init__(self, name: str, age: int):
        self._age = age
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age < 0:
            raise ValueError("age cannot be less than 0")
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


person2 = Person("Tolu", 22)
print(person2.age, person2.name)


# class Basket:

#     def basketSize(self, itemCount: list, item=None):
#         itemCount = []
#         if len(itemCount) > 3:
#             itemCount.pop(0)
#         itemCount.append(item)
#         return itemCount
#
#
# basketTest = Basket.basketSize("rice", "bread", "drink")
# print(basketTest)


class BasketSize:
    def __init__(self, size: int) -> None:
        self.size = size
        self.basket = []

    def add_item(self, item: str) -> None:
        self.basket.append(item)
        if len(self.basket) > self.size:
            self.basket.pop(0)


basketTest = BasketSize(4)
basketTest.add_item("rice")
basketTest.add_item("beans")
basketTest.add_item("dodo")
basketTest.add_item("ewaGoyin")
basketTest.add_item("softDrink")
basketTest.add_item("realDodo")

print(basketTest.basket)


class Animal:
    def __init__(self, name, bread):
        self.name = name
        self.bread = bread

    def speak(self):
        print("I am barking")


class Dog(Animal):
    def __init__(self, name, bread, color="Black"):
        super().__init__(name, bread)
        self.color = color


class Cat(Animal):
    pass


dog = Dog("Max", "GoldenDog")
dog.speak()
print(dog.name)
print(dog.bread)
