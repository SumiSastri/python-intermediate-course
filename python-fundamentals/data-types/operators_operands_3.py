# IN THIS FILE: FUNDAMENTAL CONCEPTS
# uncomment each line and click run in Pycharm terminal
# Operators & operands
# operators perform a special task between values or 2 variables
# an operand is what the operator operates on
# arithmetic operators are +/ -/ */ ** pow/ //division & double division math floor/ % modulus
# #binary operators operate on only 2 operands at all times

# OPERATORS & OPERANDS
a = 5  # a and b are operands
b = 10
c = a + b  # + / = are operators
print(a, b)
print(c)

# VALUE ASSIGNMENT OPERATOR
# compound reassignment assignment operator
f = 5
f += 2  # (add 2 to f)
f %= 3  # (f now is 7 modulus answer therefore is 1)
print(f)

# ARITHMETIC OPERATORS
print(5+2);     # addition - not to be confused with concating 2 strings
print(5-2);     # subtraction
print(5*2);     # multiplication
print(5**2);    # power of 2 - result 25
print(5**3);    # power of 3 - result 125
print(5/2);     # divide result 2.5
print(5//2);    # divide and maths floor  - result 2
print(5%2);     # modulus or remainder
d = a + 40
print(d)                # reassigment of values
e = 30 + 70 + 100       # no matter how long the statement is the operators only operate on 2 operands
print(e)


# CONCATENATION
# concatenation operator + does not print 2 different types, strings are immutable can not convert abc into a number
print(5 + int('5'))
print(str(5) + '5')
print(5 + 5)
print('5' + '5')

# replication does not matter the order as they are 2 different types the string is replicated if same type, multiplied
print('4' * 5)
print(5 * '4')
print(5*4)

#   BOOLEAN LOGIC - COMPARISON OPERATORS
#   comparison operator boolean checks (only returns true or false)

g = 5
h = 10
print(g == h)   # double equals is the comparison operator
print(g != h)   # not equal
print(g > h)    # greater than
print(g < h)    # less than
print(g <= h)   # less than or equal to
print(g >= h)   # greater than or equal to

#   LOGICAL OPERATORS - return boolean values
# NOTE: and, or, not - as words not symbols (unlike JavaScript)

i = 5
j = 10
k = 15

print(i < j and j > k)      # both must return true otherwise returns false
print(i < j) and (j > k)    # alternative syntax - to show both sides of the argument
print(i < j or j > k)       # either operator can be true or false returns true
print(i < j) or (j > k)     # alternative syntax
print(not(i > j))           # negates the logic and returns the opposite
         # and precendence if there is no not
         # otherwise not takes precedence
         # not is a unary operator others are binary

#   Membership operators prints a return of true or false in all compound variables - in/ not in
