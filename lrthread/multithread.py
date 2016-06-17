import threading

import time

import multiprocessing

from lrthread import multiprocess


def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n =0
    while n <5:
        n = n+1
        print('thread %s >>> %s' % (threading.current_thread().name,n))
        time.sleep(1)
    print('thread %s ended' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop,name='LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)

balance = 0

def change_it(n):
    global balance
    balance = balance +n
    balance = balance -n

lock = threading.Lock()

def run_thread(n):
    for i in range(100000):
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()

t1 = threading.Thread(target=run_thread,args=(5,))
t2 = threading.Thread(target=run_thread,args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)

def loop():
    x = 0
    while True:
        x = x ^ 1

for i in range(multiprocessing.cpu_count()):
    t = threading.Thread(target=loop)
    t.start()

#在多核心下，不是传统意义上的多线程，因为解释器有gil锁，实质还是单线程，不过可以通过多进程避免

#ThreadLocal


local_school = threading.local()

def process_student():
    std = local_school.student
    print('Hello, %s (in %s) ' % (std,threading.current_thread().name))


def process_thread(name):
    local_school.student = name
    process_student()

t1 = threading.Thread(target=process_thread , args=('3Serise',) , name='BMW')
t2 = threading.Thread(target=process_thread , args=('a4l',) , name='audi')
t1.start()
t2.start()
t1.join()
t2.join()

#分布式进程





