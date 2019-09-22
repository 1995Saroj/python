# This is a Python Program to implement circular queue data structure

class CircularQueue:
    def __init__(self):
        self.queue = list()
        self.head = 0
        self.tail = 0
        self.maxsize = 10
    
    def enqueue(self, data):
        if self.size() == self.maxsize - 1:
            print("The Circular Queue is already full.")
        else:
            self.queue.append(data)
            self.tail = (self.tail + 1) % self.maxsize
            return True
        
    def dequeue(self):
        if self.size() == 0:
            print("There is nothing in the Circular Queue to pop out.")
        else:
            data = self.queue[self.head]
            self.head = (self.head + 1) % self.maxsize
            return data
        
    def size(self):
        if self.tail >= self.head:
            return (self.tail - self.head)
        else:
            return (self.maxsize - (self.head - self.tail))
        
    def printQueue(self):
        print(self.queue)
        

object = CircularQueue()
object.enqueue(9)
object.enqueue(1)
object.enqueue(5)
object.enqueue(2)
object.enqueue(6)
object.printQueue()
object.enqueue(7)
object.enqueue(0)
object.printQueue()
object.dequeue()
object.printQueue()


