# IN THIS FILE:- i/o input-output
# Python has several inbuilt-methods or functions, that we have already seen

# - print() # prints the variable passed
# - type() # describes data type
# - help() # prints a list of help options
# - bool()/ dict()/ int()/ float()/ list()/ set()/ str()/ tuple() # global data-types

# THE INPUT METHOD
# input() takes a string by default, any numbers will be interpreted as strings
name = input("Please enter your name")
print('Hello ' + name)  # To prettify output, you need to leave a space within the quotes
# %s is a place holder for the output if it is a string
print('Hello %s' % name)

# int(input()) is a callback that converts the string value of input to an integer
number1 = int(input('please enter a number'))
number2 = int(input('please enter another number'))
print(number1)
print(number2)

# str() converts the number to a string
print("sum is " + str(number1 + number2))
print("sum of " + str(number1) + " and " + str(number2) + " is " + str(number1 + number2))

# %d is a place number for the output if it is a number
# the first args are the variables the second is the operator and operand required to execute output func
print("The value of %d to the power of %d is %d" % (number1, number2, number1 ** number2))
# exit() # stop the code from running on this line
# the result is the tuple of the function - this means it becomes immutable
print("Hello %s, the result of %d minus %d is %d" % (name, number1, number2, number1 - number2))
exit()
