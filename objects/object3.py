class Duck:#definition of a class
    def quack(self):#method inside of a class is always self
        #self is a reference to the object
        print('Quaaaack!')
        
    def walk(self):
        print('Walks like a duck.')
        
def main():
    prajukta= Duck()#variable called donald
    #we assign donald from the class and that makes donald an object
    #donald is now an object from the class Duck
    prajukta.quack()#the method is quack
    prajukta.walk()
    
if __name__ == '__main__': main()#auto-instantiate


    