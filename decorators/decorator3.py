import time

def elapsed_time(f): #function elapsed time wraps the pastg function in two time stamps
    def wrapper():
        t1 = time.time()
        f()
        t2 = time.time()
        print(f'Elapsed time: {(t2 - t1) * 1000} ms')
    return wrapper
#it runs the above function and prints out the elapsed time


@elapsed_time #big_sum has this decorator, it's actually wrapped in the elapsed_time wrapper
def big_sum(): # adds a whole lot of numbers and prints the sum
    num_list = []
    for num in (range(0, 10000)):
        num_list.append(num)
    print(f'Big sum: {sum(num_list)}')

def main():
    big_sum()

if __name__ == '__main__': main()
