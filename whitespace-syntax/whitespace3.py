import platform

def main():
    message()

def message():
    print('This is python {} running on {}'.format(platform.python_version(), platform.system()))
    print('Hello World!')
    if False:
        print('Line 10')
    else:
        print('Line 11')

if __name__== '__main__' : main()
   
