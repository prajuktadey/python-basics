class Duck:#definition of a class
    sound = 'Quack!'
    walking = 'Walks like a duck.'
    def quack(self):#method inside of a class is always self
        #self is a reference to the object
        print(self.sound)#called from sound
        
    def walk(self):
        print(self.walking)#called from walking 
        
def main():
    donald= Duck()#variable called donald
    #we assign donald from the class and that makes donald an object
    #donald is now an object from the class Duck
    donald.quack()#the method is quack
    donald.walk()
    
if __name__ == '__main__': main()

    