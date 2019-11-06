class Employee:

    def __init__(self, salary):
        self.salary = salary

    def __add__(self, other):
        return self.salary + other.salary

e1 = Employee(5000)
e2 = Employee(6000)
print(e1 + e2)

# print(e1 + e2) will throw an error - need a magic method

# ```
__add__
# __sub__ -
# __mul__ *
# __mod__ %
# __floordiv__

# ```