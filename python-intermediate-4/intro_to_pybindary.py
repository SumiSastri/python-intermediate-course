list1 = [10, 23, 45, 67, 88, 11, 2]

# print(55 in list1)
'''
Alogorithm statements
0. n = 55
1. sorts list -- ascending list1.sort()
2. find start position -- 0
3. last position -- len (list1) -1
4. find the mid position -- start = end // 2
5. if n == list1[mid] -- return True
6. if n> list1[mid -- start = mid + 1 
7. n list1[mid] --end = mid -1
8. continue till start <=end

'''

print(list1)
list1.sort()

def binarySearch(n):

    start = 0
    end = len(list1) -1
    while start <= end:
        mid = (start + end) // 2
        if n == list1[mid]:
            return True, mid
        elif n> list1[mid]:
            start = mid + 1
        else:
            end = mid -1
    return False

print(binarySearch(55))
print(binarySearch(45))