# Exercise 1
print("My name is Dave")
print("My Student Number is DT_001")
print("My Email Id is dave@yahoo.com")

# Exercise 2


a = 14
b = 7
print(a + b)
print(a - b)
print(a * b)
print(a // b)

print("%d + %d = %d" %(a,b,a + b))
print("%d - %d = %d" %(a,b,a - b))
print("%d * %d = %d" %(a,b,a * b))
print("%d / %d = %d" %(a,b,a // b))


# Exercise 3

for x in range (1,6):
    print("\t" * (x-1) + str(x))

# Exercise 4


print('"SDK" stands for "Software Development Kit", whereas\n"IDE" stands for "Integrated Development Environment". ')

# Exercise 5


bornIn=int(input("Enter your born in"))
agein2020 = 2020-bornIn
print("In the year 2020, you will be %d years old" %(agein2020))

# Exercise 6

name = input('Please Enter You Name ')
print('Hi %s Welcome to Python Programming :)' %(name))

# Exercise 7


amountInPounds=float(input("Please enter an amount in Pounds  "))
print("The amount you entered is  ",amountInPounds)
print("The amount in Dollars is £%.2f " %((amountInPounds)*1.45))


# Exercise 8


name=input("Enter your name  ")
studentNum=input("Enter your student Number  ")
email=input("Enter your email address   ")
print("Hello %s Thanks for Entering Your details.\n We will send you an email on %s, with subject id: %s, about further information" %(name,email,studentNum))



# Exercise 9


bornIn=int(input("Enter your born in"))
agein2020 = 2020-bornIn
print("In the year 2020, you will be %d years old" %(agein2020))


# Exercise 10


print("Doctor who Festival\nEnter  0 if none")
indvidials = int(input("Enter number of individuals"))
under16 = int(input("Enter number of under 16s"))
families = int(input("Enter number of families"))

indvidualCost = indvidials * 68
under16Cost = under16 * 32.25
familyCost = families * 42.75


print("Category Price BreakDown")
print("*" * 20)
print("Price is %.2f for %d individuals" %(indvidualCost,indvidials))
print("Price is %.2f for %d under 16s" %(under16Cost,under16))
print("Price is %.2f for %d families" %(familyCost,families))

print("Total persons are %d" %(indvidials + under16 + (families*4)))
print("Total Evenr price is £%.2f" %(indvidualCost + under16Cost + familyCost))
print("For more info and booking visit our website")



