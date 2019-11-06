userName = input ("Please enter your username ")
password = input ("Please enter your password ")

# if userName == 'student' and password == 'abc':
#     print('You are logged in'); print('Welcome to the site')
# else:
#     print('please check your login details')

if userName == 'student' and password == 'abc':
    print("'You're logged in'"); print('Welcome to the site')
elif userName == 'student' and password != 'abc':
    print('please check your password')
elif userName != 'student' and password == 'abc':
    print('please check your user name')
else:
    print('please check your login details')