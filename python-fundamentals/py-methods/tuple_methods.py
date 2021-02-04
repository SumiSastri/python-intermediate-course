# IN THIS FILE:- tuple immutability and limited methods possible
# tuples are read only

t1 = (23, 24, 25, 26, 27)
print(t1)
print(type(t1))   # TUPLE

t2 = (33, 66, 12, 'java', 55)
print(t2)
print(type(t2))  # TUPLE

t3 = (101)      # INTEGER
print(t3)
print(type(t3))

t4 = (1010000,)
print(t4)
print(type(t4))  # TUPLE

# CONCATENATION
print(t1 + t4)

# REPETITION - tuples are immutable
print(t1 * 3)
print()

# GLOBAL MIN/MAX
print(max(t1), min(t1))
print()

# SLICE
print(t2[0])
print(t2[-1])
print(t2[2:5])
print()

# value reassignment - does not happen - tuples immutable
print(t2)
print(t1)

# conversions of tuples to lists for mutation
list1 = list(t1)
list1.append(101)
t1 = tuple(list1)
del list1
print(t1)
