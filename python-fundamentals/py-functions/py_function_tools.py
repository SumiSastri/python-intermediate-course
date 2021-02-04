import functools
def even(n):
    return n % 2 == 0

def add (a,b):
    return a+b

def square(n):
    return n ** 2

def compare(a, b):
    return a if a > b else b

list1 = list (map(square, range (1,21)))
print (list1)

list3 = list(filter(even, range(1,21)))
print(list3) # returns only true values

total = functools.reduce(add, range(1, 11), 20) # takes the last argument as the start value then returns the accumulated value
print(total)

list3 = [ 12,45,67,89,11,2,34]

biggest = functools.reduce(compare, list3)
print(biggest)

smallest = functools.reduce(lambda x, y: x if x < y else y, list3)
print(smallest) # lambda is an anomymous function, replaces def and the function name4

v1 = lambda x, y: x if x < y else y, list3
smallest = functools.reduce(v1, list3)
print(smallest) #  assign lambda to a variable