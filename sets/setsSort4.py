def main():
    a = set("We're gonna need a bigger boat.")
    b = set("I'm sorry, Dave. I'm afraid I can't do that.")
    print_set(sorted(a))# to sort the string
    print_set(sorted(b))

def print_set(o):
    print('{', end = '')
    for x in o: print(x, end = '')
    print('}')

if __name__ == '__main__': main()

# each time i run it they come up in the same sorted order.
# we need to check the membership of the sets and using them as sets not as lists.
# if you want an ordered list, you'll use a list or a string.