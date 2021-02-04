# IN THIS FILE:- IF-ELSE-ELIF statement

# COMPARISON AND LOGICAL OPERATOR  with != checks username, password match
userName2 = input("Please enter your username ")    # variable assignment must be unique for each code block
password2 = input("Please enter your password ")

if userName2 == 'bob' and password2 == '123':
    #  on true value run this
    print("'You're logged in'"); print('Welcome to the site')
elif userName2 == 'bob' and password2 != '123':
    #  on true value run this
    print('please check your password')
elif userName2 != 'bob' and password2 == '123':
    #  on true value run this
    print('please check your user name')
    #  on false default value run this
else:
    print('please check your login details')