class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area_of_rectangle(self):
        aor = self.width * self.length
        return aor


class Square(Rectangle):
    def lengthSquare(self):
        return self.length ** 2


square = Square(12, 4)
print(square.lengthSquare())