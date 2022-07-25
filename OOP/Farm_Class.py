class Animal:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def speak(self, sound):
        return self.name, "usually makes", sound, "sound"

    def eating(self, food_type):
        return self.name, "likes to eat ", food_type

    def running(self, isRunning):
        if isRunning:
            return True
        else:
            return False


class Dog(Animal):
    def speak(self, sound="Bark"):
        return super().speak(sound)

    def eating(self, food_type="shit"):
        return super().eating(food_type)

    def running(self, isRunning):
        return super().running(isRunning)


dogObj = Dog("bulldog", 3, "brown")
print(dogObj.eating())
print(dogObj.speak())
print(dogObj.running(True))
