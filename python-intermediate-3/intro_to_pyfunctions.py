# Functions in python are declared with the key word def (define) and written in camelCase
# Parenthesis hold the arguments or parameters of the function
# A colon signifies the end of the function definition
# Semicolons are used to write statements in one line without a line break
# pass returns an empty function & terminates the code block
# Functions are called outside the block and are not indented

def addNumbers(): #defining the function
    pass
def addNumbers2(): # a function wiht no arguments
    print(5+20)
addNumbers2() # calling the function

def addNumbers3(a, b): # a function with required arguments
    print(a+b)
addNumbers3(10, 30)

# def addNumbers4(a, c, b =20,): # has two arguements one is required the other is default if you put c at the end the default value will be replaced
#     return a + b # passes the value to the statement that calls it
# x = addNumbers4(40,50) #holds this value in the stack memory - needs to be passed to a new variable
# print(x) # replaced the value of the default b
# print()
# print(addNumbers4(80)) # where there is a default value you can skip the default argument when you call the function
#
# function# def addNumbers5(a, c, b =20,):
#     return (a + c + b)
# y= addNumbers5(10,15)
# print(y)


def addNumbers5(*numbers): #returns a tuple with one asterisk
    sum = 0
    print(type(numbers))
    for n in numbers:
        sum += n
    return sum # takes the first value and terminates if the indentation is not aligned to for
print(addNumbers5(5, 10, 30, 50, 10 ))# print indentation adds ll the numbers

print(addNumbers5())#empty function returns zero not an error as a tuple can have zero as a value

def addNumbers6(**numbers): # keyword argument 2 asterisks return a dictionary
    sum = 0
    print(type(numbers))
    for k, v in numbers.items():
        sum += v
    return sum
print(addNumbers6(a=5, b =10, x =20, y =40))

print(addNumbers6())#empty function returns zero not an error as a dict can have zero as a value

TESTVARIABLE = 20 # GLOBAL VARIABLE IN CAPS

def changeValue():
    global TESTVARIABLE # refers to the global variable to be used within the current function scope
    TESTVARIABLE = 50 # the initial value of the global value is reassigned to 50
    print(TESTVARIABLE) # now there are no local variables so when you print it you will get empty parenthesis
    print(locals())
    # print(globals())
changeValue()
print(TESTVARIABLE)
changeValue()
print(TESTVARIABLE)

# entities/ class  - students, courses, emails - number of students - blueprint/template - class members refers to the methods and the variables
# attributes can be specific or generic - name, email, contact - variables, attributes, fields - VARIABLES
# the variable number of students is generic
# the specific variables are also called object or instance variables - they are not pure replicates but INSTANCES OF THE CLASS
# class variables are generic variables
# actions planned on data - save, modify, print, delete - functions or methods / actions or operations METHOD
# mEHTODS CAN ALSO BE SPECIFIC OR GENERIC - A SPECIFIC FUNCTION WILL HAVE DEFINED ARGUMENTS A GENERIC CAN HAVE EMPTY VARIABLES
# class methods vs instance methods
# individual students - s1/ s2 are replicates of the class / instances of the class/ individual object
# class diagram - UML - unified modelling language