# IN THIS FILE:- WHILE statement

# ITERATIONS INTRODUCTION
#  Control flow selects which statements to execute in which order
#  Iterations-loops-repetitions repeat a set of statements under some conditions or until a break/exit called
#  With repetition the flow starts with a variable assignment, a test statement is declared
#  the modifier statement executes until the program returns false

# WHILE statement - repeats a set of statements while some condition is true

# variable assignment
initial_count = 1   # variable assignment

while initial_count <= 10:     # test statement declared with colon
    print('Hello - %d' % initial_count)  # statement body
    #            test the boolean before running, test the boolean before each iteration of the loop
    initial_count += 1          # modifier statement - perform statement body till false returned
print('programme completed')
# exit()                        explicit exit function call


file5 = open('content.txt')
count = 0
line = file5.readline()
while line != '':
    print(line.strip('\n'))
    count += 1
    line = file5.readline()
print("Number of lines is %d" % count)
file5.close()
