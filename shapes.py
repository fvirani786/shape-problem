

class Shape:
    def __init__(self, color):
        self.color = color

    def area(self):
        return 0

    def perimeter(self):
        return 0

    def __str__(self):
        return f"Shape color: {self.color}"

class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

