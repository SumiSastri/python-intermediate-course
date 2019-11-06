name = input("Please enter your name")
# number1 = input('please enter a first number')
# input() takes a user input as a string
# convert the string to a number
number1 = int(input('please enter a first number'))
number2 = int(input('please enter a second number'))
print(number1 + number2)

print ("sum is " + str(number1 + number2))
print("sum of " + str(number1) + " and " + str(number2) + " is " + str(number1 + number2))
# print ("sum of .. and .. is ..") # the elipsis is a place holder you can replace it with %d which is a place holder for an integer %f for floats
print ("sum of %d and %d is %d" %(number1, number2, number1+number2)) # the result is the tuple of the function
print ("Hello %s, the sum of %d and %d is %d" %(name,number1, number2, number1+number2))
