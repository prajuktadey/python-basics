def main():
    x=kitten()
    print (type(x), x) 
    
def kitten():
    print('Meow!')
    return 32
    
if __name__=='__main__': main()