

l1 = [1, 2, 3, 4.2, 4]                   # homogemous list
l2 = [1, 'london', 3.2, 'python', True]  # heterogenous list
l3 = ['Python', 'is', 'not', 'like', 'JavaScript']

print(l1)
print(l2)
print(l3)
print()

for n in l1:
    # print(n)
    print(n, end='\t')
    # default print is vertical - change to horizontal
print()
print()


l2 = [x for x in l2 if x != 3.2]         # list comprehension with a for loop
print(l2)
print()

for x in enumerate(l2):
    print('enumerate x', x)            # shows the position and value at the same time
print()


l3 = [x for x in l3 if x != 'like']     # list comprehension
print(l3)
print()

for x in enumerate(l3):
    print(x)                            # shows the position and value at the same time

for n in l3:
    print(n, end='\t')                  # prints one element at a time vertically change with the end = command


