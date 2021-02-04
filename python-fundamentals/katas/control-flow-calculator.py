def calculate(num1=18, num2=27, operand=''):
    if operand == '+':
        return num1 + num2
        print('add', num1 + num2)
        # print("%d + %s + %d = %d" % (num1, operand, num2, num1 + num2))

    elif operand == '-':
        return num1 - num2
        print('subtract', num1 - num2)

    elif operand == '*':
        return num1 * num2
        print('multiply', num1 * num2)

    elif operand == "//":
        return num1 // num2
        print('divide', num1 // num2)

    else:
        print('use a valid calculation')


calculate(24 + 24)
