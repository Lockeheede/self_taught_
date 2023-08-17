class Hexagon():
    def __init__(self, s):
        self.sides = s

    def calculate_perimeter(self):
        return self.sides * 6

x = input("Give me the length of the sides of a hexagon ")
x = float(x)
hexagon = Hexagon(x)
print(hexagon.calculate_perimeter())
