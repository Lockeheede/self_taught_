class Shape():
    def __init__(self, w, l):
        self.width = w
        self.length = l
    def what_am_i(self):
        print("I am a shape")

class Square(Shape):
    def calculate_perimeter(self):
        return 2 * (self.length + self.width)
    def change_size(self, sz):
        self.length = self.length + sz
        self.width = self.width + sz
    def what_am_i(self):
        print("I am a square")
    

class Rectangle(Shape):
    def calculate_perimeter(self):
        return 2 * (self.length + self.width)
    def what_am_i(self):
        print("I am a rectangle")

a_square = Square(20, 20)
a_rect = Rectangle(15, 20)
a_shape = Shape(10, 12)

sqr_per = a_square.calculate_perimeter()
rec_per = a_rect.calculate_perimeter()

print("The square's perimeter is", sqr_per)
print("The rectangle's perimeter is", rec_per)

a_square.change_size(5)
sqr_per = a_square.calculate_perimeter()
print("The square's perimeter is", sqr_per)

a_square.what_am_i()
a_shape.what_am_i()
