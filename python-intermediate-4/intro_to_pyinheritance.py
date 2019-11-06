# class A Class B class B(A)  parent and child, super is the parent class, subclass is child, data flows from parent to child, if the method is private you will not inherit it  will not access it base is the parent, derived is the child

# Class C Class A Class B(A) Class C (B) classes can be inherited several times down the tree - multi-level data flow is unidirectional from parent to child, when a method is called, the traversal is from child upwards to parent to execute

# Class C (A,B) - traverses in multiple inheritance first to the first argument, the second argument and the global object

# built in vs object global - print is a function not  a global object

# Network of inheritance will follow the path of the arguements passed


class Shape:
    def getSides(self, sides = 2): # prevents method overloading using a default and an if block
        self.length = float(input('Enter length'))
        if sides == 2:
            self.width = float(input('Enter width')) # needs to be indented one more


class Rectangle(Shape):
    def findArea(self):
        return self.length * self.width

class Square(Shape):
    def findArea(self):
        return self.length ** 2

print(Rectangle.__bases__) # trace back the parent
print(Square.__bases__)
print(Shape.__bases__)
print(Rectangle.__mro__) # method resolution
print(Square.__mro__)
print(Shape.__mro__)
exit()

print('Area of rectangle')
r1 = Rectangle()
r1.getSides(2) # we dont have to use 2 as an argument as it is default
print("Area of rectangle is %.2f" %(r1.findArea()))

print()
print('Area of square')
s1 = Square()
s1.getSides(1) # as this is not the default it passes 1 arguement
print("Area of square is %.2f" %(s1.findArea()))




'''
FUNCTION/ METHOD OVERLOADING
print()
print('hello')
print("Area of square is %.2f" %(s1.findArea()))

OPERATOR OVERLOADING
print(5+5)
print('5'+'5')
'''


