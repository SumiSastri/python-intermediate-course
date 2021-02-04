# number1 = int(input('please enter a first number '))
# number2 = int(input('please enter a second number '))
# print(number1)
# print(number2)
#
# def add(number1, number2):
#     return number1 + number2
# print (add(1,1))


selectOperation = input("ggg")
print selectOperation
exit()

class Calculator:
    '''this class processes a simple calculations'''

    def add(number1, number2):
        return number1 + number2

    def __init__(self,number1, number2, operation):
     self.number1 = number1
     self.number2 = number2
     # operation = ['add', 'subtract' ]

     if operation == 'add':

        print (self.add(number1, number2))
#
# elif operation == 'subtract'
#     def subtract(num1, num2):
#         return num1 - num2
# subtract()
# print ("sum is " + str(number1 + number2))
#
# elif print('this is not a valid operation)
#

#    @classmethod
#     def number1(cls):
#         print(int(input('please enter a first number ')))
#     def number2(cls):
#         print(int(input('please enter a second number ')))

# calculate = Calculator


