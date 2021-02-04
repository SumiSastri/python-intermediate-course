class Employee:
    def __init__(self, salary):
        self.salary = salary

    def __add__(self, other):
        return Employee(self.salary + other.salary)

    def __str__(self):
        return str(self.salary)

e1 = Employee(5000)
e2 = Employee(10000)
e3 = Employee(20000)
print(e1 + e2+ e3)

##########################
exit()

class Employee:
    def __init__(self, salary):
        self.salary = salary

    def __add__(self, other):
        return self.salary + other.salary

e1 = Employee(5000)
e2 = Employee(10000)
print(e1 + e2)

##########################
exit()
class Employee1:
    def __init__(self, salary):
        self.salary = salary

e1 = Employee1(5000)
e2 = Employee1(10000)
print(e1 + e2) #ERRRO soma objetos