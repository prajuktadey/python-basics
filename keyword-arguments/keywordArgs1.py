def main():
    kitten(Buffy='meow', Zilla='grr', Angel='rawr')# this is a dictionary
    
def kitten(**kwargs):
    if len(kwargs):
        for k in kwargs:
            print('Kitten {} says {}'.format(k, kwargs[k]))
    else: print ('Meow.')  
    
if __name__=='__main__' : main()

# list arguments have one asterisk before them
# we use two asterisks for a dictionary
    

