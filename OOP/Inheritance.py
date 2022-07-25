class Dog:
    species = "Cani familiaries"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name, "is ", self.age, "years old"

    def speak(self, sound):
        return self.name, "says", sound


class GoldenRetriever(Dog):
    def speak(self, sound="Bark"):
        return super().speak(sound)


golden = GoldenRetriever("bubby", 5)
print(golden.__str__())
print(golden.speak())
print(golden.species)
