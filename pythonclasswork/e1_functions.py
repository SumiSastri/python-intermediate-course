
def addnumbers6(**values):
    sum = 0
    print(values.items())
    for k, v in values.items():
        sum += v
    return sum

print(addnumbers6(a=10, b=20))
exit()

def addnumbers5(*values):
    sum = 0
    for n in values:
        sum += n
    return sum

print(addnumbers5(5,11))
exit()