# an instance of a class is called an object
# it's created by calling a class itself as if it were a function

class Animal:
    def __init__(self, type, name, sound):# init: speacial name for a class function which operates as an initializer, or a constructor 
        # pass it three arguments
        # self, type, name and sound are used to initialize object variables
        self._type = type
        self._name = name
        self._sound = sound # object variables all have an underscore in the beginning

    def type(self):
        return self._type

    def name(self):
        return self._name

    def sound(self):
        return self._sound

def print_animal(o):# expects an animal object and prints the animal
    if not isinstance(o, Animal):
        raise TypeError('print_animal(): requires an Animal')
    print('The {} is named "{}" and says "{}".'.format(o.type(), o.name(), o.sound())) # we use those getters in order to access the variables

# object is created by using the class name as if it were a function name
def main():# created two objects
    #initialising it with various parameters
    a0 = Animal('kitten', 'fluffy', 'rwar')# this calls the contructor
    a1 = Animal('duck', 'donald', 'quack')
    print_animal(a0)
    print_animal(a1)
    print_animal(Animal('velociraptor', 'veronica', 'hello'))

if __name__ == '__main__': main()

# function parameters work exactly like assignments in Python