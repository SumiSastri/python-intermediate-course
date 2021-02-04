# IN THIS FILE:- WHILE-AND statement

# variable assignment method 1
# password = ""
# count = 0

password, num_of_attempts = "", 0  # variable assignment method 2 - several variables assigned in one statement

while password != "abc" and num_of_attempts < 5:  # test statement declared with colon

    password = input("Enter password ")  # not the loop variable nor the modifier it is only the input value
    num_of_attempts += 1  # not the loop variable nor the modifier it is only a count
    print('you %d attempts left' % (
                5 - num_of_attempts))  # modifier statement - perform statement body till false returned

#     while, if else one code block
if password == 'abc':  # modifier statement - perform statement body till false returned
    print('Password correct with %d attempts left' % (
                5 - num_of_attempts))  # modifier statement - perform statement body till false returned
else:
    print('Password failed')  # modifier statement - perform statement body till false returned

# print relates to the while and block

print('Password correct with %d attempts left' % (5 - num_of_attempts)) if password == 'abc' else print(
    'Password failed')  # modifier statement - perform statement body till false returned
