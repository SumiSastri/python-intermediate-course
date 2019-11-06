def square(n):
    try:
        assert isinstance(n,int), "value must be numeric"
        assert n<10, "value must be less than 10"
        print(int(n)**2)
    except TypeError as t:
        print("Invalid Type" + str(t.args))
    except ValueError as v:
        print("Value Error" + str(v.args))
    except Exception as e:
        print(e.args)
    else:
        print("Else - Program executed without exception")
    finally:
        print("Finally - Program always executed")

square(15)
square(5)
square(5.5)
square('5')
square('abc')

exit()
def square(n):
    try:
        print(float(n)**2)
    except TypeError as t:
        print("Invalid Type" + str(t.args))
    except ValueError as v:
        print("Value Error" + str(v.args))
    except Exception as e:
        print(e.args)

square(5)
square(5.5)
square('5')
square('abc')