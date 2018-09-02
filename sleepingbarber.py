import queue
from threading import Thread,Lock
import time
import random


class Barber(Thread):
    def __init__(self, waiting, barber):
        Thread.__init__(self)
        self.waiting = waiting
        self.barber = barber
        self.sleeping = True  # barber is sleeping

    def run(self):
        while True: #if customer in waiting room
            self.sleeping = False  # barber wakes up
            customer = self.waiting.get() 
            print("Customer {} sat down in barber chair {}\n".format(customer, self.barber))
            Customer.chair = True  # customer is in barber chair
            time.sleep(random.randint(2,5))
            print("Barber {}: Finished cutting {}, next customer!\n".format(self.barber,customer)) 
            if self.waiting.empty():
                print("Oh, no one is here")
                print("I'm finished!")
                print("Barber {} is sleeping\n".format(self.barber))    
                        


class Customer(Thread):

    def __init__(self, customer, waiting):
        Thread.__init__(self)
        self.customer = customer
        self.waiting = waiting
        self.chair = False  # barber chair is empty
        self.lock = Lock()
    def wait(self):
        time.sleep(random.randint(2,5)) 

    def run(self):
        with self.lock:
            if not self.waiting.full():  # if waiting room isn't full
                self.waiting.put(self.customer)  # add customer into waiting room
                print("Customer {} sat down in waiting room\n" .format(self.customer))
            else:
                print ("Waiting room is full, customer {} is leaving\n".format(self.customer))


if __name__ == "__main__":
    barber = [1, 2, 3, 4, 5]
    customers = 4, 5, 3, 1, 2, 6, 7, 9, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 25,26,27,28,29,30
    waiting = queue.Queue(15)  # max size of 15
    customer_threads = []
    barber_threads = []

    for c in customers:
        t1 = Customer(c, waiting)
        customer_threads.append(t1)
        t1.setDaemon = True

    for c in barber:
        t = Barber(waiting, c)
        barber_threads.append(t)
        t.setDaemon = True

    
    for c in barber_threads:
        c.start()
    for c in customer_threads:
        c.start()

    for c in barber_threads:
        c.join()

    for c in customer_threads:
        c.join()
