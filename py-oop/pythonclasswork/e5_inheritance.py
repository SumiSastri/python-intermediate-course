class Shape:
    def getSides(self, noOfSides = 2):
        self.length = float(input("Enter Length"))
        if noOfSides == 2:
            self.width = float(input("Enter Width"))

class Rectangle(Shape):
    def calculateArea(self):
        return self.length * self.width

class Square(Shape):
    def calculateArea(self):
        return self.length ** 2



print(Square.__bases__)
exit()

r1 = Rectangle()
r1.getSides(2)
print("Area of rectangle is %.2f" %(r1.calculateArea()))

s1 = Square()
s1.getSides(1)
print("Area of square is %.2f" %(s1.calculateArea()))

#print("hello", "world, end= '\t'', sep=':')