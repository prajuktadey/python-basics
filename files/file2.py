#writing text files
def main():
    infile = open('C:\\learning\\python-basics\\files\\lines.txt', 'rt')
    outfile = open('C:\\learning\\python-basics\\files\\lines-copy.txt', 'wt')
    for line in infile:
        print(line.rstrip(), file=outfile)
        print('.', end='', flush=True)
    outfile.close()
    print('\ndone.')

if __name__ == '__main__': main()