def main():
    x=5
    kitten(x)
    print(f'in main: x is {x}')   
    
def kitten(a):
    a=3
    print('Meow!')
    print (a)
    
main()

#in most call by value languages a value is passed but not the object itself
#the value that is passed is a copy of the value in most programming languages
# in python, the no copy is sent
 