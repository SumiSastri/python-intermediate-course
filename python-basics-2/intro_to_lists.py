# read only value - not changing lists
# writable and mutable (synonyms)
list1 = [1, 2, 3, 4.2, 4] # homogemous list
list2 = [1, 'london', 3.2, 'python', True] # heterogenous list

print(list1)
print (list2)
print (len(list1)) #number of elements in a collection or compound variables
print ('*' * 20)
print (max(list1)) # function max and min apply only to homogeneous list
print (min(list1)) # mixed type will give an error
print (list1 + list2) # concats the 2 lists
print (list2 * 3)  # repetition prints list 3 times
print()
# SLICING
print (list1[0]) # returns element from index
print (list1 [-1]) # returns a left-to right index starts at -1 not -0
print (list1 [0:3]) # returns 0 1 and 2 index as the last is excluded
print (list1 [:3]) # auto starts at index zero
print (list1 [2:]) # from position 2 onwards if you want the last number, upper limit now includes last number
print (list1 [1:3]) # returns index 1 and 2 and exludes 3
print (list1 [ -4: -1]) # returns -3 to -1 as the last number is excluded

print()
# LIST METHODS, METHODS ARE SPECIFIC FUNCTIONS ARE GENERIC
# functions like min, max, len (built in methods that can be used with all data types)
# list methods only are for lists
list1.append(33) # adds element at the end of the
# list1.append(66, 77) # can only add one at a time you will get an error
list1.append([66,99]) # changes the list to a heterogenous list and adds it as a nested list
print(list1)
list1.extend([88, 99]) # the extend method adds it as homogeneous element
print(list1)
list1.insert(3,111)# first param is the index and the second is the number to insert
print(list1)
list1[3:3] = [222, 333] # to insert multiple values use slicing and assigns values to this position
print(list1)
# if you do not do 3:3 it will replace index 3 with the value, this is the reason why the upper limit not taken
# if you do 3:6 then you will get the numbers replacing indexes 3, 4 and 5
list1[4] = 777
print(list1)

print()
list1.pop()  # default is  end of the list
print(list1)

list1.pop(-2)
print(list1)
# list1.pop(2)
# print(list1)

x = list1.pop(-2)
print(list1)
print(x)

list1.extend([23,45, 92,1, 2, 3])
print(list1)
list1.remove(4.2) # specify the element not the index
print(list1) # if the element does not exist you will get an error
list1.remove(1) # removes the first occurance of the
print(list1)
list1 = [ x for x in list1 if x != 23] # list comprehension
print(list1)

list1.sort()# prints list in ascending order by default and applicable to homogenous lists
list1.sort(reverse=True) # descending order also for homogenous lists
print(list1)
list2.reverse() # reverses the list without ordering it for heterogenous lists
print(list2)

print()
print(list1) # print list when mutated to see what is in the list
del list1[2:6] # deletes the range except the upper limit
print(list1)

for x in enumerate(list1):
    print(x) # shows the position and value at the same time

for n in list1:
    print(n, end = '\t') # prints one element at a time vertically change with the end = command


