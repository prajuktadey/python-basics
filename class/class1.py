class Duck:# name of the class
    sound = 'Quack quack.'
    movement = 'Walks like a duck.'

    def quack(self):# methods
        # first parameter of a method is always self.
        print(self.sound)

    def move(self):# methods
        print(self.movement)

def main():
    donald = Duck()
    donald.quack()# invoked the object method
    donald.move()# invoked the object method

if __name__ == '__main__': main()
