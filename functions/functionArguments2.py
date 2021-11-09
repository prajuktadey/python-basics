def main():
    kitten(5,6)

def kitten(a,b,c=0):
    print('Meow.')
    print(a,b,c)
    
if __name__== '__main__': main()

# arguments with defaults must be at the end of the list