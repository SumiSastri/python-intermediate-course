# Print - cheat sheet
# end='\t\t'
# sep='/'

# % the percentage sign wrapped in a string means this is a placeholder

# %s string - it prints the arg as a string by default
# %s%s - describes 2 args with string type
greet = 'Hello'
name = 'Anita'

#  it is wrapped in quotes there is no comma
#  space after quotes and before open parenthesis - namespaces comma separated
print('%s %s' % (greet, name))

#  the %.2f represents one argument
#  float describes the expectation of the arg
#  the float is converted into a string - parse float
num1 = 10.89
num2 = 20.52
add = num1 + num2
print(" £%.2f " % float(add))

# £%.6f describes the number of decimal places in the float
num3 = 10.892345
num4 = 20.523423
add_34 = num3 + num4
print(" £%.6f " % float(add_34))


# £%.d integer with a parse int
num5 = 2384756.2345
num6 = 9384757373.6789
multiply = num5 + num6
print(" £%d " % int(multiply))

# £%.d note -  ignores all decimals
num7 = 2384756.2345
num8 = 9384757373.6789
multiply_78 = num7 + num8
print(" £%d " % int(multiply_78))
