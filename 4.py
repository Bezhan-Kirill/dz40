import threading
import random

lock = threading.Lock()


def fill_out_list():
    with lock:
        file = open('text_file.txt', 'w')
        for i in range(0, 10):
            x = random.randint(1, 100)
            file.write(str(x) + " ")
        file.close()


def write_simple_number():
    file = open('text_file.txt', 'r')
    list = file.read()
    file.close()
    file = open('simple_numbers.txt', 'w')
    for x in list.split():
        if find_simple_number(int(x)) == True:
            file.write(x + " ")
    file.close()


def find_simple_number(x):
    if x == 3 or x == 5 or x == 7:
        return True
    else:
        for i in range(2, 9):
            if x % i == 0:
                return False
    return True


def write_factorial():
    file = open('text_file.txt', 'r')
    list = file.read()
    file.close()
    file = open('factorial.txt', 'w')
    for x in list.split():
        file.write(str(factorial(int(x))) + " ")
    file.close()


def factorial(x):
    factorial_x = 1
    while x > 0:
        factorial_x = factorial_x * x
        x -= 1
    return factorial_x


thread_1 = threading.Thread(target=fill_out_list)
thread_2 = threading.Thread(target=write_simple_number)
thread_3 = threading.Thread(target=write_factorial)

thread_1.start()
thread_2.start()
thread_3.start()

thread_1.join()
thread_2.join()
thread_3.join()
