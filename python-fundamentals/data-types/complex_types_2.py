# IN THIS FILE: COMPLEX DATA-TYPES
# uncomment each line and click run in Pycharm terminal
# This is a basic introduction to the non-scalar data-types in Python

# LISTS - linear, 0 indexed, mixed types, mutable, traversable
# (an array in JavaScript) - can order a list

k = [56, 23, 15, 20, 15]  # elements all of the same type but the data type is a list
print(type(k))
print(type(k))

l = [56, 'apples', 12, True, 18.7, True]  # mixed types square brackets elements separated by commas
print(l)
print(type(l))

# TUPLES (linear, 0 indexed, immutable, traversable )
# makes an array immutable so you don't need to duplicate the array as in JavaScript methods - map, filter, reduce

m = (56, 23, 15, 20, 15)  # tuple - syntax ordinary parenthesis comma separated elements
print(type(m))

# DICTIONARIES(non-linear, unordered key-value pairs, unique-keys not the values which can be duplicated\
# (an object in JavaScript) - can't order a dictionary

o = {'id': 2, 'name': 'david'}  # dictionary # mutable # key-value pair
print(o)
print(type(o))

# SETS, SEQUENCES, COLLECTIONS (unordered elements of unique elements)
# n is a key word and can not be used as a variable

_my_set = {56, 23, 15, 20, 15}  # looks like a dictionary but does not have key-value pairs
print(_my_set)
print(type(_my_set))