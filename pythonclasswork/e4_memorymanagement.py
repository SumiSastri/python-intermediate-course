import sys
x=5
print(sys.getrefcount(5)) #33  => stack (pilha)
y=5
print(sys.getrefcount(5)) #34
z= [5,10,15,20,5]
print(sys.getrefcount(5)) #36

class Test:
    def __init__(self):
        self.x = 5

t1 = Test()
t2 = Test()
print(id(t1) == id(t2)) #False

print(sys.getrefcount(5)) #38
del t2 #remove da memoria    => limpa a memoria
print(sys.getrefcount(5)) #37

print(id(x)) #501565136 => Heap (area da memoria)
print(id(t1.x))
print(id(x) == id(t1.x)) #True

print(id(x) == id(x)) #True
print(id(x) == id(z)) #False
print(id(x) == id(z[0])) #True