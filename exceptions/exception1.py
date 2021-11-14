# exceptions are a powerful runtime eroor reporting mechanism commonly used in object oriented systems

def main():
    try:
        x=5/0
    except ValueError:
        print('I caught a Value Error')
    except ZeroDivisionError:
        print('Do not divide by 0')
    else:
        print('Good Job!')
        
if __name__ == '__main__': main()
