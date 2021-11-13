def main():
    seq = range(11)# 0 to 10
    from math import pi
    seq2={x for x in 'superduper' if x not in 'pd'}
    print_list(seq)
    print_list(seq2)

def print_list(o):
    for x in o: print(x, end = ' ')
    print()

if __name__ == '__main__': main()

# a list comprehension is a list created based on another list or iterator.