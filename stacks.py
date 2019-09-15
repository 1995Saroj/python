# This is a Python program to implement stack data strucute.

class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
    
    def isEmpty(self):
        return self.items == []

    def getStack(self):
        return self.items
    
object = Stack()
print(object.isEmpty())
object.push(1)
object.pop()
object.push("UTA")
print(object.getStack())