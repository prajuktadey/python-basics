def main():
    x=kitten()
    print (type(x), x) 
    
def kitten():
    print('Meow!')
    return [23,56,89]# we can return a list
    
if __name__=='__main__': main()