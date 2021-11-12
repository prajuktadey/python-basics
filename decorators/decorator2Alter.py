def f1(f):# f1 is going to take an argument which it is going to use as a function
    def f2():
        print('This is before the function call')
        f()
        print('This is after the function call')
    return f2

@f1 #decorator
def f3():
    print('This is f3')
    
f3()

# a function within a function

# the syntax is you have to have the decorator
# followed directly by the function definition
# and it takes that function and passes it
# as an argument to the decorator function
# and it returns and assigns that name of f3 to the wrapper itself
# we cannot call f3 directly, we can only call it through the wrapper
# f3 now is wrapped inside the decorator function

