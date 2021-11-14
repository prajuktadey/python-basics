# exceptions are a powerful runtime eroor reporting mechanism commonly used in object oriented systems

import sys# to know more about unknown errors
def main():
    try:
        x=5/0
    except ValueError:
        print('I caught a Value Error')
    except:
        print(f'unknown error: {sys.exc_info()}')# to know more about errors not know to us
    else:
        print('Good Job!')
        
if __name__ == '__main__': main()
