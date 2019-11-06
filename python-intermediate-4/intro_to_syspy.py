import sys

a = 5
print(sys.getrefcount(5))
b=10
print(sys.getrefcount(10))
print()
c = [5,10,15,5]
print(sys.getrefcount(5))
print()
class MyClass:
    def __init__(self):
        self.x = 5

m1 = MyClass()
m2 = MyClass()

print(sys.getrefcount(5))
c[-1] =55
print(sys.getrefcount(5))
print()
print(id(m1))
print(id(m2))
print()
print(id(m1.x))
print(id(m2.x))
print()
print(id(a) == id(m1.x))
del m2
print(sys.getrefcount(5))

# Batch upload data and balance load
# __ del __ you have to define the method that you want - it needs to be called - if you write pass it will not be executed - needs to be called