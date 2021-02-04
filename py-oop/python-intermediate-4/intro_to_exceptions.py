def square(n):
    try:
        assert isinstance (n, int), "please provide a number"
        assert n < 25, 'Number must be below 25'
        list1 = [12,46, 67, 89 ]
        # print(list1[6])
        print(int(n)**2)# indentation different
    except AssertionError as ae:
        print('assertion failed as %s' %(ae.args))
    except ValueError as v:
        print('invalid value provided') # raise exception with nested block
    except IndexError as i:
        print('please check the list index')
    except Exception as e:
        print('something went wrong, %s' %(e.args))
    else:
        print('programme completed successfully')
# square(10) # error at design time and compile time
# square('10') # error at run-time when program compiled and executed
    finally:
        print('Thanks for using this program') # executed irrespective of the exceptions

# square('10ab') # something went wrong & completed with error arguments
# square(50) # will fail on the condition that it is not below 25