class Student:
    '''This class holds methods to register new students'''

    #Generic atributes
    __noOfStudents = 0 #private: 2underscore nao permite manipular o valor da vbariavel fora da classe

    def __init__(self, id, name, email):
        self.id = id
        self.name = name  #Specific atribute
        self.email = email
        Student.__noOfStudents += 1 #Para generic class vc precisa usar o nome da classe. nao permite usar self.

    def printData(self):
        print("Id is %d and Name is %s and your email is %s" %(self.id, self.name, self.email))

    @classmethod #Nao permite override eh um metodo private
    def printNoOfStudents(self):
        print("Number of students is %d" % (Student.__noOfStudents))

if __name__ == "__main__" : #if the current file (module) is being executed
    s1 = Student(1001, "Jim", "jim@gmail.com") #Construtor (__init__)
    s1.printData()
    s2 = Student(1002, "Maria", "maria@gmail.com") #Construtor (__init__)
    s2.printData()
    Student.printNoOfStudents()
    print(Student.__doc__)
    print(Student.__module__)
    print(Student.__name__)
    print(Student.__bases__)
    print(Student.__dict__)
    print(s1.id == s2.id)
