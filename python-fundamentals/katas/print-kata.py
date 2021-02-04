# Exercise 1 - print strings of a name, student id and email
print("My name is Dave")
print("My Student Number is DT_001")
print("My Email Id is dave@yahoo.com")

# Exercise 2 - print arithmetic operators and operands (+/-/* and //)

a: int = 14
b: int = 7

print(a + b)
print(a - b)
print(a * b)
print(a // b)

print("%d + %d = %d" % (a, b, a + b))
print("%d - %d = %d" % (a, b, a - b))
print("%d * %d = %d" % (a, b, a * b))
print("%d / %d = %d" % (a, b, a // b))

# Exercise 3 - print the numbers with a hard return and in steps

# for num in range(1, 5):
#     print("\n" * num + str(num))

for num in range(1, 6):
    print("\t" * num + str(num))

# Exercise 4 - print with line break

print('"SDK" stands for "Software Development Kit", whereas\n"IDE" stands for "Integrated Development Environment". ')
