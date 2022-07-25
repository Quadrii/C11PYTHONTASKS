class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        return self.name, " is ", self.age, "years old"

    def coloInfo(self):
        return self.name, "coat is ", self.coat_color

    def sound(self, sound):
        return self.name, " makes a", sound, " sound"


bulldog = Dog("Bull Dog", 3, "black")
print(bulldog.coloInfo())
print(bulldog.description())
print(bulldog.sound("gbu gbu"))
