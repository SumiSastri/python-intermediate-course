# password = ""
# count = 0
password, count = "", 0
while password != "abc" and count <5: # loop variable does not change
    password = input("Enter password ") # modifier changes the value of the loop statement
    count += 1 # not the loop variable nor the modifier it is only a count

#     print('you %d attempts left' %(5 - count))
# if password == 'abc':
#         print('Password correct in %d attempts')
# else:
#         print ('Password failed')

print('Password correct in %d attempts' %(5-count)) if password == 'abc' else print('Password failed')