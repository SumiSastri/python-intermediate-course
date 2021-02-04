# IN THIS FILE: FUNDAMENTAL CONCEPTS
# uncomment each line and click run in Pycharm terminal
# Variables, primitive types and print function

# DYNAMICALLY TYPED
# Python is a dynamically typed object-oriented language
# This means the type of data is inferred and compiled there is no explicit need to define the type
# All Python methods and functions are stored in the global object
# Functions or methods stored at the global level have reserved key words

# Print is a global function - it logs output to the console
# print('hello world')

# NOTE:
# print takes some additional arguments to prettify output
# sep defines how the 2 lines should be separated
# end='\t\t' at the end of the character leave a space
# sep is the way to assert the input value of the separator instead of white space
# print ("sum of .. and .. is ..")
# the ellipsis is a place holder you can replace it with
# %d which is a place holder for an integer
# %f for floats

# Uncomment this for a demo on printing - more in the strings section
a = 20
b = a
c = 4.7
print(a, b, c, sep=':')     # sep is the way to assert the input value of the separator instead of white space
d = True
e = False
print(d, e, sep='/')
i = "You can use single quotes for apostrophe's (sic) within double quotes"
print(i)
k1 = "Print demo 1"
j = 'Josephine Karlsson'
print(k1)
print()                     # an empty print starts a new line
print(c, end='\t\t')        # instead of the new line default it ends the line with 2 tab spaces
                            # end is the end character
print()
# neater way to print different lines
k2 = 'Print demo 2'
print(k2); print(a, b, c); print(d,e); print(j) # semicolons also print separate lines

# help() #help is a global function

# VARIABLES - name space naming conventions
# As in all programming languages data can be stored to a variable
# The assignment operator is a single equals sign a space between the operator and operand
# Naming conventions snake_case all lower case
# Use alphabets to start, can't start with a number or special characters
# store_some_number = 10
# can start with an underscore
# _store_my_string = 'stores any value I require'
# can start with camelCase - but not the convention
# myFunc ='this is more JavaScript than Python'
# reserved key words can not be used as variables, code will not compile
# help('keywords') # Use the global help function to list all keywords

# SCALAR DATA TYPES

# NUMBERS - integers and floats
a = 5
print(a)
print(type(a)) # type() is a function that defines the type of data

# you can print 2 values in one command - white space is important in Python
# no space between print and parenthesis
a = 5
b = 10
print(a, b)

c = 4.7
print(c)
print(type(c)) # type needs to be explicitly called as Python is dynamically typed

# value reassignment - you can reassign values in Python
a = 20
b = a
print(a)

# BOOLEANS
d = True
e = False
print(d, e, sep='/')
print(type(d))  # type() takes a single arg

# STRINGS - indexed and immutable

f = "You can use double quotes for a string"
print(f)
print(type(f))
g = "You can use single quotes within double quotes to 'emphasise' a point "
print(g)
h = 'You can use "double quotes" within single quotes as well'
print(h)
i = "You can use single quotes for apostrophe's (sic) within double quotes"
print(i)

character_a = 'Josephine Karlsson'
series = 'Engrenages'
print(character_a, series, sep=':')
print(character_a, series, end='\t\t') # end='\t\t' at the end of the character leave a space
print(type(character_a))

# value reassignment - you can reassign any type in the values in Python
character_a = 'Josephine Karlsson'
character_b = character_a # print an empty line to prettify into 2 lines
print(character_b)
series = "'Engrenages'"
print()
print(series)

demo_one='Demo print multiple lines with semicolons'
character_a = 'Josephine Karlsson'
series = '"Engrenages"'
print(demo_one); print(character_a); print(series);

comment = '''Demo 2: Multi-line print with 3 single quotes & hard returns
Who agrees?
Josephine Karlsson made watching 'Engrenages' addictive'''
print(comment)
