# tuples are read only

t1 = (23, 24, 25, 26, 27)
t2 = (33, 66, 12, 'java', 55)
t3 = (101,) becomes an integer if (101)
t4 = (101,)

print(t1)
print(t2)
print (t3)
print (type(t2))
print (type(t3))
print (type(t4))

print(t1 + t4)
print(t1 * 3)
print(max(t1), min(t1))

print()

#slicing
print(t1[0])
print(t1[-1])
print(t1[2:5])

# conversions of tuples to lists for mutation
list1 = list(t1)
list1.append(101)
t1 = tuple(list1)
del list1
print(t1)