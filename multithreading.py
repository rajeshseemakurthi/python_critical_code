"""Multithreading concept implementted on Python classes"""


from threading import Thread
import time

class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            time.sleep(0.2)

class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            time.sleep(0.2)

t1=Hello()
t2=Hi()

t1.start()
time.sleep(0.1)
t2.start()
time.sleep(0.1)

t1.join()
t2.join()

print("This is the concept of MultiThreading in Python code")

