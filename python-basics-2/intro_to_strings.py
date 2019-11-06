# strings are read only - it creates a new string with methods
s1 = '''Python is a programming language - Programming AAAAaaah ?'''
print(s1)
print(len(s1)) #prints length of all caracters as well as white space
print(s1.count('a')) # finds all the instances of a in the string
print(s1.count('programming')) # finds all the instances of the word - case sensitive
print()
print(s1.find('a')) # position of the first occurance of the alphabet
print (s1. find('a', 11 )) # find a from the 11 onwards to the upper limit
print (s1.find ('a', 11, 17)) # does not exist the upper limit is excluded if it is 18 then diff answer
print()
# STRING METHODS
print(s1.upper())
print(s1.lower())
print(s1.title())
print(s1.capitalize())
print(s1.swapcase)
print()
print(s1)

# REASSIGN VALUE
s1 = s1.title()
print(s1)
print(s1.replace(' ', '-')) # need white space if no space then hypen for all the characters
print()
# Extract data based on a boolean value
print(s1.startswith('python'))
print(s1.startswith('P'))
print(s1.endswith('e'))
print()
print(s1.split()) # splits on white space with a comma by default
print(s1.split('y')) # breaks in multiple occurances
list1 = (s1.split('y'))
print(list1)

s2 = 'london academy of IT'
print(s2)
v1, v2, v3, v4 = s2.split()
print(v1) # you have to have the assign the number of variables to the number split each word is like an index
print(v2)
print(v3)
print(v4)
# print(v5) # this will give you an error there are not enough variables to unpack
print('-'.join(s1))
s3 = 'radar'
s4 = 'abcd1234'
s5 = '1234'

#STRIPS - cleaning data
print(s3.lstrip('r')) #remove from left start
print(s3.lstrip()) # strip nothing, does nothing but compiles inefficient in run time
print(s3.rstrip('r')) #remove from right start
print(s3.strip('r')) #remove from both ends
print()

#Boolean values - good for data-validation
print(s3.isalnum()) # is alpha numeric
print(s4.isalpha()) # is alpha numeric
print(s5.isalpha()) # is alpha numeric
print(s5.isdigit()) # is alpha numeric

#Slicing - good for validation, finding particular values, cleaning
print()
print(s1[0])
print(s1 [-1])
print(s1[2:10])