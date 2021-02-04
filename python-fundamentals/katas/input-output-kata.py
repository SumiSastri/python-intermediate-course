# Exercise 5 - collect user inputs - name with output welcome greeting

name = input('Please Enter You Name ')
print('Hi %s Welcome to Python Programming :)' %(name))


# Exercise 6 - collect user name, student number and email, output the result back

name = input("Enter your name  ")
studentNum = input("Enter your student Number  ")
email = input("Enter your email address   ")
print(
    "Hello %s Thanks for Entering Your details.\n "
    "We will send you an email on %s, with subject id: %s, very soon"
    % (name, email, studentNum))
