# #Exercise 1
class Calculator:
    def getInput(self):
        self.firstNum = int(input("Enter First Number"))
        self.secondNum = int(input("Enter First Number"))
        self.choice = input("Enter choice(1 - Add, 2 - Substract, 3 - Multiply , 4 - Divide :)")
        if self.choice == '1':
            print("%d + %d = % d" %(self.firstNum, self.secondNum, self.firstNum + self.secondNum))
        elif self.choice == "2":
            print("%d - %d = % d" % (self.firstNum, self.secondNum, self.firstNum - self.secondNum))
        elif self.choice == "3":
            print("%d * %d = % d" % (self.firstNum, self.secondNum, self.firstNum * self.secondNum))
        elif self.choice == "4":
            print("%d / %d = % d" % (self.firstNum, self.secondNum, self.firstNum / self.secondNum))

    def add(self):
        return self.firstNum + self.secondNum

    def sub(self):
        return self.firstNum - self.secondNum

    def mult(self):
        return self.firstNum - self.secondNum

    def div(self):
        return self.firstNum / self.secondNum


c1 = Calculator()
c1.getInput()

#Exercise2

class Fruit:
    def __init__(self,name, color, flavour, poisonous):
        self.name = name
        self.color = color
        self.flavour = flavour
        self.poisonous = poisonous

    def description(self):
        print("I am a %s and I taste %s" %(self.name, self.flavour))

    def is_edible(self):
        print("I am edible") if not self.poisonous else print("Don't eat me! I am super poisonous")

f1 = Fruit("apple", "red", "sweet", False)
f1.description()
f1.is_edible()

#Exercise3

class Polygon:

    def __init__(self,noOfSides):
        self.noOfSides = noOfSides
        self.sides = [0 for i in range(noOfSides)]

    def inputSides(self):
        self.sides = [float(input("Enter side %d" %(i+1)) ) for i in range(self.noOfSides)]

    def dispSides(self):
        for n in self.sides:
            print(n,'\t',end='')

class Triangle(Polygon):

    def __init__(self):
        super().__init__(3)

    def calcArea(self):
        a,b,c = self.sides
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        print("Area of triangle is %.2f" %(area))

p=Triangle()
p.inputSides()
p.dispSides()
p.calcArea()



