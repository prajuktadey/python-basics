import platform

def main():
    message()

def message():
    print('This is python {} running on {}'.format(platform.python_version(), platform.system()))

if __name__== '__main__' : main()
   
