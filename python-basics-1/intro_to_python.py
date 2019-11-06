#print('hello world') #function print sends output to console
# single line comment
'''comments for multi-line
in single quotes '''
"""or in double 
quotes as well"""
# Storing values in variables - value = assigned to a variable
# Naming conventions - start with lower case or camelCase, or snake_case (below python3)
# Use alphabets to start, can't start with a number or special characters, can start with an underscore

a = 5
b = 10
c = 4.7
d = True
e = False
g = 'Python'
h = "Programming language"
i = "'Python' is a \"programming\" language" # single quote for emphasis or to escape out of an apostrophe
j = '''Python is
 a programming language''' # store multi-line values

print(a)
print(b)
print (a, b)
print(c, end ='\t\t') # instead of the new line default it ends the line with 2 tab spaces - end is the end character
print(a, b, c, sep = ':') # sep is the way to assert the input value of the separator instead of white space
print(d, e, sep ='/')
print(); print (i); print(); print(j) # can not have multiple lines but can do with semicolon

a = (20) #reassigns value scalar variables hold only one value at all times
# compound variables can hold one or more values

k = [56, 23, 15, 20, 15] # mutable #list
l = (56, 23, 15, 20, 15) #tuple # immmutable
x = {56, 23, 15, 20, 15} #set # removes duplicatates
z = [56, 'apples', 12, True, 18.7, True] #mutable # list
m = {'id':2, 'name':'david'} #dictionary # mutable # key-value pair

print(k, l, x, z, m, sep ='\n' )
print(type(a)); print(type(c)); print(type(d)); print(type(g)); print(type(k)); print(type(m)); 
print(type(l))
print(type(m), type(x))
