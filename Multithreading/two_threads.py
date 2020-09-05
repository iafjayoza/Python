from threading import *
from time import sleep

class Hello(Thread):
    def run(self):
        for i in range(50):
            print("Hello")
            sleep(0.5)


class Hi(Thread):
    def run(self):
        for i in range(50):
            print("Hi")
            sleep(0.5)

t1 = Hello()
t2 = Hi()

t1.start()
sleep(0.2)
t2.start()

t1.join()
t2.join()
print("Bye")