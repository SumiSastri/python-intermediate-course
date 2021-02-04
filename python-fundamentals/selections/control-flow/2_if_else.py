# IN THIS FILE:- IF-ELSE statement

# COMPARISON AND LOGICAL OPERATOR - performs an exact case match
userName = input("Please enter your username ")     # variable assignment
password = input("Please enter your password ")     # variable assignment

if userName == 'student' and password == 'abc':     # test statement declared with colon
    #  on true value run suite 1
    print('You are logged in'); print('Welcome to the site')
    #  on false value run suite 2
else:
    print('please check your login details')
