import e2_oop

s1 = e2_oop.Student(1003, "Dan", "dan@gmail.com")
s1.printData()
e2_oop.Student.printNoOfStudents()
print(e2_oop.Student.__module__) #Note que eh module, pois estamos em outro file diferente de onde a classe foi criada.

########
exit()
'''
#if __name__ == "__main__" : #if the current file (module) is being executed
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
'''