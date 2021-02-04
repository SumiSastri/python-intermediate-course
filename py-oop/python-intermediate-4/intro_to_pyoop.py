class Student: #PascalCase - eg. StudentDetail
    ''' documentation string - this class processes student data - write the global written first'''

    __noOfStudents = 0 # this is a global variable within the scope of the class Student called the generic class variable

    def __init__(self, id, name, marks): # the arguement are not intiantiated these are specific variables to the object
        self.id = id # lexical self now intiatiates the arguements
        self.name = name # self is s1 which is initatiated by
        self.marks = marks
        Student.__noOfStudents += 1 # right click refactor and rename - this now becomes a private variable that can not be used outside the class - it specifies the access with the 2 underscores within the class but not out of the class - you can not read or write

    def printData(self):
        print("Id is %d and Name is %s marks is %d" %(self.id, self.name,self.marks))

    @classmethod # generic methods use decorators - the decorator decorates the method inside it it is an attribute applied to a method
    def printNoOfStudents(cls):
        print("no of students is %d" %(Student.__noOfStudents))

    def __del__(self): # destructor method - when object gets removed from memory
        Student.__noOfStudents -=1


# create an object - which is the variable s1 - assign it to the student class which triggers the init method implicitly
# creates the instance of the class - two double underscores or magic methods call the method automatically depending on the requirement
# when an object is created - a variable that intiantiates  object  as a constructor!
# self is a variable which holds the current object which triggers the init method - it is the same as lexical this

s1 = Student(5001, 'James', 100) # calling class name as a method
s1.printData() # explicit calling of data
s2 = Student (123, 'Ajay', 50)
s2.printData()
# print(Student.__noOfStudents)
# Student.__noOfStudents = 99 # the class variable can be overwritten outside the class - it needs to be protected with 2 underscores in the init method - errors will show
# print(Student.__noOfStudents) # class variable
Student.printNoOfStudents()
del s2
Student.printNoOfStudents()
print(Student.__name__) # name of student
print(Student.__doc__) # domentation string
print(Student.__module__) # file name if it was in introtopy.py or if same file returns __main
print(Student.__bases__)  # gives you the parent class
print(Student.__dict__) # gives you the meta data of the class

#ENCAPSULATION - defines the class variables and methods, restricts the accessibility of variables and methods - data hiding
# Python is reference based not value based - as it refers to the objects they point to
# Scalar and compound variables are all held in the heap
# Bbecuase everything is an object and points to the reference in the heap, it is also delinked from the heap
# Once a variable is not needed it is automatically cleaned from the heap - garbage collection is automatic in python, c sharp, java not the older languages
# RAM - Stack - points to the value 5 everything is reference based in Python, not value based
# Heap -  a = 5 scalar value is stored in the heap unlike other programming  languages in a randomised fashion

