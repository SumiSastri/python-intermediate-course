# # IN THIS FILE:- Functions and function definition

# Methods are pre-written, inbuilt functions in the global object, they are immutable
# Functions are programming blocks of logic defined by the user and are mutable
# Functions in python are declared with the key word def (define) and written in snake_case
# Naming convention snake_case but camelCase acceptable
# Parenthesis hold parameters of the function
# A colon signifies the end of the function definition
# The function body takes the params as arguments and defines what the logic is relating to the params
# Semicolons are used to write statements in one line without a line break
# pass returns an empty function & terminates the code block
# Functions are called outside the block and are not indented


# function definition
def add_nums_1():
    pass


# function definition without args
def add_nums_2():
    print(5 + 20)


# function call
add_nums_2()


# function definition with args
def add_nums_3(a, b):
    print(a + b)
    #  print does not save the result to memory, return does - return does not take parenthesis
    return a + b


# variable assignment to the result
result = add_nums_3(10, 30)
print('result', result)
print()


# default args - not sure what this is doing - check
# def add_nums_3a(a, c, b=20, ):
#     return a + c + b
#
#
# y = add_nums_3a(10, 15)
# print('y', y)


# - not sure what this is doing - check
# def add_nums_3b(a, c, b=20, ):
#     x = add_nums_3b(40, 50)
#     # holds this value in the stack memory - needs to be passed to a new variable
#     print('x', x)
#     # replaced the value of the default b
#     print()
#     print('add', add_nums_3b(80))
#     # where there is a default value you can skip the default argument when you call the function


# kwarg - key word argument returns a tuple with one asterisk
def add_nums_4(*numbers):
    sum = 0
    print('type of add_nums_4', type(numbers))
    for n in numbers:
        sum += n
    return sum  # takes the first value and terminates if the indentation is not aligned to for


print('add_nums_4', add_nums_4(5, 10, 30, 50, 10))
# empty function returns zero not an error as a tuple can have zero as a value
print('add_nums_4', ())
print()


# kwarg - key word argument returns a tuple with one asterisk
def add_nums_5(*values):
    sum = 0
    print('type of add_nums_5', type(values))
    for n in values:
        sum += n
    return sum


print('add_nums_5', add_nums_5(5, 11))
print()


# kwarg keyword argument 2 asterisks return a dictionary (object)
def add_nums_6(**values):
    sum: int = 0
    print('type of add_nums_6', type(values))
    print(values.items())
    for key, values in values.items():
        sum += values
    return sum


print('add_nums_6', add_nums_6(a=10, b=20))
# empty function returns zero not an error as a dict can have zero as a value
print(add_nums_6())
print()


# kwarg keyword argument 2 asterisks return a dictionary (object)
def add_nums_7(**nums):
    sum = 0
    print('type of add_nums_7', type(nums))
    print(type(nums))
    for key, values in nums.items():
        sum += values
    return sum


print('add_nums_7', add_nums_6(a=5, b=10, x=20, y=40))
print(add_nums_7())  # empty function returns zero not an error as a dict can have zero as a value
print()

# String constant as a variable

TEST_VARIABLE = 20


def changeValue():
    # refers to the global variable to be used within the current function scope
    global TEST_VARIABLE
    print('TEST1', TEST_VARIABLE)
    # the initial value of the global value is reassigned to 50
    TEST_VARIABLE = 50
    # now there are no local variables so when you print it you will get empty parenthesis
    print('TEST2', TEST_VARIABLE)
    # print('LOCALS', locals())
    # print('GLOBALS', globals())


changeValue()
print('TEST3', TEST_VARIABLE)
