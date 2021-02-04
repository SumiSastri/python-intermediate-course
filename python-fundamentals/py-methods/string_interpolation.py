# IN THIS FILE:- string-interpolation or inbuilt functions for strings

# strings are indexed, immutable and read only - string traversal and iteration possible
# string interpolation are methods performed on strings
# the string therefore has to be assigned to a variable for the methods to work
# Formatting: upper(), lower(), capitalize(), swapcase(), title() - Title Case
# Boolean search: startswith(), endswith(), isalpha(), isalnum(), isdigit()
# Search/Count: len(), find(), count(),
# Interpolation: split(), slice([num1:num2]), join(), strip(), replace(),


# SEARCH & COUNT
s1 = '''Python is a programming language - Programming AAAAaaah ?'''
print(s1)                       # variable assignment
print(len(s1))                  # prints length of all characters as well as white space (57)
print(s1.count('a'))            # finds all the instances of a in the string (8)
print(s1.count('programming'))  # finds all the instances of the word - case sensitive - finds a substring

print()

print(s1.find('a'))             # position of the first occurrence of the alphabet @10
print(s1.find('a', 11))         # find a from the 11 onwards to the upper limit @17
print(s1.find('a', 11, 17))     # (-1) does not exist the upper limit is excluded if it is 18 then diff answer
print(s1.find('a', 11, 18))     # zero indexed so finds the position @17
print()

# FORMATTING
print(s1)                       # Compare output against the original string
print(s1.upper())
print(s1.lower())
print(s1.title())
print(s1.capitalize())
print(s1.swapcase())
s1 = s1.title()  # REASSIGN VALUE
print(s1)
print(s1.replace(' ', '-'))     # need white space if no space then hyphen for all the characters
print()

# BOOLEAN SEARCH                Extract data based on a boolean value - - good for data-validation
print(s1.startswith('python'))
print(s1.startswith('P'))
print(s1.endswith('e'))
print()

s3 = 'radar'
s4 = 'abcd1234'
s5 = '1234'
print(s3, s3.isalnum())             # contains alphabets and numbers
print(s3, s3.isalpha())             # is alphabet
print(s3, s3.isdigit())             # is a number
print()
print(s4, s4.isalnum())
print(s4, s4.isalpha())
print(s4, s4.isdigit())
print()
print(s5, s5.isalnum())
print(s5, s5.isalpha())
print(s5, s5.isdigit())

# INTERPOLATION                     good for validation, searches and cleaning

# SLICE
print()
print(s1[0])                        # Slices on index value @ first position
print(s1[-1])                       # Slices on index value @ last position
print(s1[2:10])                     # Slices on index value @ after position 2 and before position 10
print()

# SPLIT
# print(s1.split(5:11)) INVALID SYNTAX
s2 = 'Python not Monty Python'
print(s2)
print(s2.split())                   # splits on white space returns a list of elements by default
print()
v1, v2, v3, v4 = s2.split()         # variable assignment for each element
print(v1)                           # not zero-indexed or split on white space
print(v2)
print(v3)
print(v4)
# print(v5)                         # 4 words, 4 variables, this will throw error not enough variables to unpack
print()
print(s2.split('y'))                # breaks in multiple occurrences
list1 = (s2.split('y'))
print()

# JOIN
print(list1)
print('-'.join(s2))                 # joins with a dash
print()

# STRIP
s6 = 'radio-radar'
print(s6, s6.lstrip())                  # strip nothing, does nothing but compiles inefficient in run time
print()
print(s6, s6.strip('r'))                # remove from both ends
print(s6, s6.lstrip('r'))               # remove from left start
print(s6, s6.rstrip('r'))               # remove from right start
print()
print(s6, s6.strip('a'))                # remove from both ends - does nothing only removes first and last letter
print(s6, s6.lstrip('a'))               # remove from left start
print(s6, s6.rstrip('a'))               # remove from right start
print()

# IMMUTABLITY

print(s1, s2, s3, s4, s5, s6)

word = 'dog'
split_word = word.split()
print('Hello %s' % (split_word))
reverse_word = split_word.reverse()
# returns null value as it can not be mutated ( in this case the split word can not be reversed)
print('Hello %s' % (reverse_word))