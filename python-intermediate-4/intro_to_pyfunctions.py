def addNumbers():# def (define) function name in  CamelCase() parenthesis hold the arguments/parameters colon
    pass # is the empty block - it is a placeholder for an empty function will terminate return with tab


def addNumbers2(): # no arguments
    print(5+20)
addNumbers2() # call the function outside the block - so not indented

def addNumbers3(a, b): # required arguments, if you don't pass the arguments you get a traceback error
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


def addNumbers5(*numbers): # this is a tuple, and the sum is being added the asterisk is any number of variable arguements
    sum = 0
    print(type(numbers))
    for n in numbers:
        sum += n
    return sum # takes the first value and terminates if the indentation is not aligned to for
print(addNumbers5(5, 10, 30, 50, 10 ))# print indentation adds ll the numbers
print(addNumbers5()) # will return zero as a tuple can hold zero values

def addNumbers6(**numbers): # keyword argument returns a dictionary
    sum = 0
    print(type(numbers))
    for k, v in numbers.items():
        sum += v
    return sum
print(addNumbers6(a=5, b =10, x =20, y =40))
print(addNumbers6()) # will return zero as a dict can hold zero values

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