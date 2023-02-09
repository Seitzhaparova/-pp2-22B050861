class Shape:
    def __init__(self, length):
        self.length = length
    def area(self):
        print(0)
class Square(Shape):
    def area(self):
        print(self.length * self.length)
c = Shape(5)
c.area()
c = Square(5)
c.area()
    