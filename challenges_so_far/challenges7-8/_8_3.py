class Triangle():
    def __init__(self, h, b):
        self.height = h
        self.base = b

    def area(self):
        return (self.height * self.base) / 2

triangle = Triangle(3,6)
print(triangle.area())
