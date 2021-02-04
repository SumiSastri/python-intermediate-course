# Exercise 11


fname = input("Please enter your first name")
lname = input("Please enter your last name")
print("Your full name is %s %s" %(fname.upper(),lname.upper()))
print("Ypur initials are %s %s" %(fname[0].upper(), lname[0].upper()))
print("First name length is %d letters " %(len(fname)))
print("Last name length is %d letters" %(len(lname)))
print("Your full name length is %d letters" %(len(fname)+len(lname)))
print("Your firstname starts with %s" %(fname[0].upper()))
print("Your firstname ends with %s" %(fname[-1].upper()))
print("Your lastname starts with %s" %(lname[0].upper()))
print("Your lastname ends with %s" %(lname[-1].upper()))
print("First name indexes are 0 - %d" %(len(fname)-1))
print("Last name indexes are 0 - %d" %(len(lname)-1))


# Exercise 12

monthsList=["January","February",'March',"April","May","June","July","August","September","October","November","Deember"]
monthNumber = int(input("Enter the month"))
print("Month %d is %s" %(monthNumber,monthsList[monthNumber-1]))


# Exercise 13

number=int(input("Enter a number  "))
print("Number entered is %d "%(number))
number=int(number)
if number%2==0:
    print("Number is even")
else:
    print("Number is odd")



# Exercise 14

age= int(input("Enter your age"))
if age >60:
    price = 6/3
elif age >16 and age <60:
    price =6
else:
    price =6/2


# Exercise 15

weight = float(input("Enter Your weight in (Kg:)"))
height = float(input("Enter Your height in (m:)"))
bmi = weight/(height **2)

if bmi <18.5 :
    category = "Underweight"
elif 18.5<= bmi <= 24.9 :
    category = "Normal"
elif 25 <= bmi <=-29.9 :
    category ="Overweight"
else:
    category = "Obese"

print("Your BMI is %.2f" %(bmi))
print("You fall in the '%s' range" %(category))


# Exercise 16

answer = input("Would you like to see comedy (Yes/No)?")
if answer.casefold() =="yes" : #casefold for case insensitive comparison
    print("You might like either Yes Minister or SPAMalot")
else:
    answer = input("Would you like to see musical (Yes/No)?")
    if answer.casefold() == "yes":
        print("You might like either  Les Miserables or Mamma Mia")
    else:
        print("You might like either  The Woman in Black or Macbeth")


# # Exercise 17

for x in range(0,10):
    print(x)

# Exercise 18

for x in range(9,-1,-1):
    print(x)


# Exercise 19

for x in range (1,6):
    print("*" * x)


# Exercise 20

for x in range (1,10):
    print(x, end ='\t')
    if x %3 == 0:
        print()


# Exercise 21

name = input("Please enter your name:")
print("Encrypted form is %s%s%s" %(name[0], (len(name)-2)*"*"  ,name[-1]))


# Exercise 22

start = int(input("Enter the first amount in Celsius:"))
end = int(input("Enter the last amount in Celsius:"))
print("CELCIUS\t\tFARENHEIT")
for x in range(start,end +1):
    print("%d\t\t%.2f" %(x,(x*9/5)+32))


# Exercise 23

moviesDict ={"Sean Connery": "From Russia With Love",
             "Roger Moore": "Live and Let Die",
             "Pierce Brosnan":"Die Another Day",
             "Daniel Craig":"Skyfall"
             }
score = 0
for x in range(1,5):
    actor = input("Attempt %d - Name an actor " %(x))
    if actor in moviesDict:
        print("Well done %s was Bond in %s" %(actor,moviesDict[actor]))
        score += 1
    else:
        print("Sorry. %s hasn’t played Bond as far as I know." %(actor))
print("You got %d out of 4." %(score))