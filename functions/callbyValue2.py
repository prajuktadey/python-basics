def main():
    x=[5] #making 'x' a list
    y=x #assigned the value of x in y
    y[0]=3#assigmed a list element but only in y
    # found out that the value of both of them was chaged
    
    print(id(x))
    print(id(y))
    print(x)
    print(y)
    #kitten(x)
    #print(f'in main: x is {x}')   
    
def kitten(a):
    print(id(a))#the id here should be different from the id assigned to x but is not
    a=3
    print(id(a))
    print('Meow!')
    print (a)
    
main()

#in most call by value languages a value is passed but not the object itself
#the value that is passed is a copy of the value in most programming languages
# in python, the no copy is sent
 