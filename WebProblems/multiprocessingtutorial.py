from multiprocessing import Process, Value, Array, Lock
from multiprocessing import Queue
import time
import os
def adduser(x):
    return x + 1
processes = []
num_processes = os.cpu_count()
#create a process
for i in range(num_processes):
    p = Process(target=adduser)
    processes.append(p)
for p in processes:
    p.start()
for p in processes:
    p.join()
def add1(user, lock):
    for i in range(10):
        time.sleep(0.1)
        for i in range(len(user)):
            user[i] += 1
        lock.acquire()
        user.value += 1
        lock.release()
if __name__ == "__main__":
    lock = Lock()
    shared_array = Array('d', [0.0, 100.0, 200.0])
    print('array is', shared_array[:])
    shared_user = Value('i', 0)
    print('First user is', shared_user.value)
    p1 = Process(target=add1, args=(shared_user, shared_array, lock))
    p2 = Process(target=add1, args=(shared_user, shared_array, lock))
    p1.start()
    p2.start()
    try:
        p1.join()
    except:
        print("UNABLE to join")
    try:
        p2.join()
    except:
        print("UNABLE to join")
    print("End user is", shared_user.value)
    print("Ending array is", shared_array[:])
def cpu_line(numbers, queue):
    for i in numbers:
        queue.put(i * i)
def shorten_list(numbers, queue):
        for i in numbers:
            queue.put(i *-1)
if __name__ == "__main__":
    numbers = range(1,9)
    q = Queue()
    p1 = Process(target = cpu_line, args=(numbers, q))
    p2 = Process(target = shorten_list, args=(numbers, q))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
