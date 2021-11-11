def main():
    x=kitten()
    print (type(x), x) #<class 'NoneType'> None because we do not have any return type
    
def kitten():
    print('Meow!')
    
if __name__=='__main__': main()