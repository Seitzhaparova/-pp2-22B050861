class Point():
    def __init__(self,x, y):
        self.x =x
        self.y =y
    def show(self):
        print(self.x, end=" ")
        print(self.y)
    def move(self, x1, y1):
        self.x += x1
        self.y += y1
    def dist(self, Point):
        print(abs(Point.x - self.x), end= " ")
        print(abs(Point.y - self.y))

c= Point(1,1)
d=Point(5,5)
c.show()
c.move(2,2)
c.show()
c.dist(d)            