def main():
    a = set("We're gonna need a bigger boat.")
    b = set("I'm sorry, Dave. I'm afraid I can't do that.")
    print_set(a)
    print_set(b)

def print_set(o):
    print('{', end = '')
    for x in o: print(x, end = '')
    print('}')

if __name__ == '__main__': main()

# a set is like a list that does not allow duplicate elements
# i get an unordered list of the unique characters in each string
# each time i run it they come up in a different order.