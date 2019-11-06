# file1 = open('content.txt', 'w') # filename, filemode = w write mode, create new if file doesnt exist overwrites the existing file
# file1.write('this is a test program to check .txt file creation \n')
# file1.close() # creates file in the same folder

# file2 = open('content.txt', 'a') # filename, filemode, a = append mode - updates content if file exists or creates if it does not exist - it is a string
# file2.write('python is cool \n')
# file2.close() # need to close otherwise it keeps loading in the memory and is inefficient

# file3 = open('content.txt', 'r') # file name, filemode - r - read mode (default mode)
# data = file3.readlines()# returns content as a list
# file3.close()
# print(data)

file4 = open('content.txt')
data = file4.read() # returns the content as a string - the backslash n is resolved as a new line
print(data)
file4.close()

file5 = open('content.txt')
count = 0
line = file5.readline()
while line != '':
    print(line.strip('\n'))
    count += 1
    line = file5.readline()
print("Number of lines is %d" %(count))
file5.close()