def main():
    seq = range(11)# 0 to 10
    seq2=[x* 2 for x in seq]
    print_list(seq)
    print_list(seq2)

def print_list(o):
    for x in o: print(x, end = ' ')
    print()

if __name__ == '__main__': main()

# a list comprehension is a list created based on another list or iterator.