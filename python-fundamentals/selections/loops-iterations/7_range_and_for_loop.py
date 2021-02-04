# IN THIS FILE:- range
#  Ideal for lists - adds the range key word to the for-loop
#  Syntax for x in y where for and in range():

for n in range(10):
    print('Hello - %d' % n)

for n in range(1, 10):
    print('Hello - %d' % n)

for n in range(1, 21, 3):  # range and 3rd value is step value
    print(n, end='\t')

for n in range(50, -1, -1):
    print(n, end='\t')

list1 = [45, 23, 45, 21, 66, 82]

for x in list1:  # x is assigned to each element of the list
    print(x)
