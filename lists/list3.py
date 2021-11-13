def main():
    seq = range(11)# 0 to 10
    from math import pi
    seq2=[round(pi, i) for i in seq] # pi rounded to each number from 0 to 10    print_list(seq)
    print_list(seq2)

def print_list(o):
    for x in o: print(x, end = ' ')
    print()

if __name__ == '__main__': main()

# a list comprehension is a list created based on another list or iterator.