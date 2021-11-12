def f1(f):# f1 is going to take an argument which it is going to use as a function
    def f2():
        print('This is before the function call')
        f()
        print('This is after the function call')
    return f2

def f3():
    print('This is f3')
    
x=f1(f3)
x()

# a function within a function