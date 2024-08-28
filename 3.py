import threading
import random

list_a = []

lock = threading.Lock()


def fill_out_list():
    with lock:
        for i in range(0, 5):
            list_a.append(random.randint(1, 10))


def find_sum():
    print(sum(list_a))


def find_summ():
    print(sum(list_a) / 5)


thread_1 = threading.Thread(target=fill_out_list)
thread_2 = threading.Thread(target=find_sum)
thread_3 = threading.Thread(target=find_summ)

thread_1.start()
thread_2.start()
thread_3.start()

thread_1.join()
thread_2.join()
thread_3.join()
