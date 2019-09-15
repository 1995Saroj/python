# This is a Python program to implement queue data structure

class Queue:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def enqueue(self, item):
        self.items.insert(0, item)
    
    def dequeue(self, item):
        self.items.pop()
    
    def size(self):
        return len(self.items)

    def printQueue(self):
        for item in self.items:
            print(item)
    
object = Queue()
print(object.isEmpty())
object.enqueue(1)
object.enqueue("UTA")
object.printQueue()
print(object.size())    