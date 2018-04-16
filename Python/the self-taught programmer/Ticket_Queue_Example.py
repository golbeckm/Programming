
import time
import random


class Queue:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def simulate_line(self, till_show, max_time):
        person_queue = Queue()
        tix_sold = []

        for index in range(10):
            person_queue.enqueue("person" + str(index))

        t_end = time.time() + till_show
        now = time.time()
        while now < t_end and not person_queue.is_empty():
            now = time.time()
            r = random.randint(0, max_time)
            time.sleep(r)
            person = person_queue.dequeue()
            print(person)
            tix_sold.append(person)
            
        return tix_sold

queue = Queue()
sold = queue.simulate_line(5,1)
print(sold)


            
    