# IN THIS FILE:- List methods
# False friend to string methods
# similar (all global methods = print(), len() plus slice([num1:num2])

# False friend to arithmetic operators
# similar - all global plus min(), max()
# gotchas - * is not multiplication but repetition

# List exclusive methods:

l1 = [1, 2, 3, 4.2, 4]                   # homogemous list
l2 = [1, 'london', 3.2, 'python', True]  # heterogenous list
l3 = ['Python', 'is', 'not', 'like', 'JavaScript']

print(l1)
print(l2)
print(l3)
print()

# SEARCH & COUNT
# functions like len (built in methods that can be used with all data types)
print(len(l1))                   # number of elements in a collection or compound variables - result 5
print(max(l1))                   # function max and min apply only to homogeneous list - result 4.2
print(min(l1))                   # mixed type will give an error - result 1
print(max(l3))                   # max number of characters - result JavaScript
print(min(l3))                   # min number of characters - result not (should be is?)
# print(max(list2))                   # errors - only available for homogenous list types
# print(min(list2))                   # errors - only available for homogenous list types
print()

# SORT
l1.sort()                       # prints in ascending order by default - [1, 2, 3, 4, 4.2]
print(l1)
# l2.sort()                             # errors out with mixed-list
# print(l2)
l3.sort()                       # title case & alphabetical order default - ['JavaScript', 'Python', 'is', 'like', 'not']
print(l3)
print()

# REVERSE
l1.reverse()                    # see reverse of mutated version as well
print(l1)
l2.reverse()                    # available for mixed lists
print(l2)
l3.reverse()                     #  see reverse of mutated version as well
print(l3)
print()

l1.sort(reverse=True)           # descending order also for homogenous lists
print(l1)
# l2.sort(reverse=True)                 # errors out
# print(l2)
l3.sort(reverse=True)           # descending order also for homogenous lists
print(l3)

# print(list1)

# CONCATENATION
print(l1 + l2 + l3)              # concats the 2 or more lists
print()

# SLICE
print(l3[0])                     # returns element from index - result Python
print(l3[-1])                    # returns a left-to right index starts at -1 not 0 - result JavaScript
print(l3[0:3])                   # returns includes 0 index excludes 3 - result: Python is not
print(l3[:2])                    # auto starts at index zero
print(l3[2:])                    # from position 2 onwards includes -1
print(l3[1:3])                   # returns includes 1 excludes 3 - result is not
print(l3[-4:-1])                 # returns -3 to -1 as the last number is excluded - result is not like
print()

# REPETITION
print(l2 * 3)                    # repetition prints list 3 times in the same list - appends it
print('*' * 20)                  # in a list it is not a pure multiplication but repetition, for a star use as string
print()


# EXCLUSIVE LIST METHODS

# APPEND
l2.append(33)                      # adds element at the end of the list
print(l2)
# list1.append(66, 77)                  # errors can only add one at a time you will get an error

l2.append([166, 199])              # changes the list to a mixed list and adds it as a nested list
print(l2)

# EXTEND
l3.extend([88, 99])                 # the extend method adds it as homogeneous element
print(l3)
l1.extend([23, 45, 92, 1,  200000, 30000])
print(l1)
print()


# INSERT
print('*' * 20)
l2.insert(3, 111)                   # first param is the index and the second is the number to insert
print(l2)
# note value of l2 is reassigned so result now [1, 'london', 3.2, 111, 'python', True, 33, [66, 99]]

l3[3:3] = [222, 333]                # to insert multiple values use slicing and assigns values to this position
print(l3)
# note value of l3 is reassigned so result now ['Python', 'is', 'not', 222, 333, 'like', 'JavaScript', 88, 99]

# if you do not do 3:3 it will replace index 3 with the value, this is the reason why the upper limit not taken
l3[3] = [589375696873475]
print(l3)

# if you do 3:6 then you will replace indexes 3, 4 and 5 with values described
l3[3:6] = ['clean', 'this', 'up']
print(l3)
print()


# POP
print('*' * 20)
l3.pop()                              # default is  end of the list
print(l3)
l3.pop(-3)
print(l3)
l3.pop(4)
print(l3)

# Reassignment gotchas - the value assigned is the value popped
l4 = l3.pop()
print(l3)
print(l4)
print()

# POP vs. REMOVE
l1.remove(4.2)                         # specify the element not the index
print(l1)                              # if the element does not exist you will get an error

l1.remove(1)                           # removes the first occurrence of the
print(l1)

# POP vs. REMOVE vs DELETE

del l1[2:6]                            # deletes the range except the upper limit
print(l1)

print('*' * 20)
# REVERSE
l1.reverse()                           # reverses into descending order
print(l1)
l2.reverse()                           # available for mixed lists
print(l2)
l3.reverse()                            # not a simple order reverse - reverses title case and alphabetically
print(l3)

