def main():
    f=open('c:\\learning\\python-basics\\files\\lines.txt')
    for line in f:
        print(line.rstrip())
        
if  __name__== '__main__': main()