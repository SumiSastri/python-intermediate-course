class calculator:
    def __init__(self):
        self.choice = int(input("Enter choice 1-Add, 2-Sub, 3-Mult, 4-Div"))
        self.number1 = input("First number")
        self.number2 = input("Second number")
        if self.choice == 1:
            print("Sun is d%" %(self.add()))
        elif self.choice == 2
            print("Diference is d%" % (self.sub()))
        elif self.choice == 3
            print("Mult is d%" % (self.mult()))
        elif self.choice == 4
            print("Div is d%" % (self.div()))

    def add(self):
        return self.number1 + self.number2

    def sub(self):
        return self.number1 - self.number2

    def mult(self):
        return self.number1 * self.number2

    def div(self):
        return self.number1 / self.number2

exit()
'''        
        result = calculator(oper, num1, num2)
        return result
    
    if 0<= oper <5:
        if oper == 1:
            return self.num1 + num2
        elif oper == 2:
            return num1 - num2
        elif oper == 3:
            return num1 * num2
        elif oper == 4:
            return num1 / num2
    else:
        print("Invalid date, please input again")
        inputdata()



result = inputdata()
print(result)
'''