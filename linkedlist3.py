# This is a python rogram to search a specific item
# in a singly linked list and return true if the item is found otherwise return's false


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def iterateItem(self):
        current = self.tail
        while current:
            value = current.data
            current = current.next
            yield value
        
    def appenditem(self, data):
        node = Node(data)
        if self.head:
            self.head.next = node
            self.head = node
        else:
            self.tail = node
            self.head = node
        self.count += 1
    
    def searchItem(self, value):
        for node in self.iterateItem():
            if value == node:
                return True
            else:
                return False

item = linkedList()
item.appenditem("Standford University")
item.appenditem("Harvard University")
item.appenditem("Boston University")
for i in item.iterateItem():
    print(i)
if item.searchItem("Standford University"):
    print("\nTrue")
else:
    print("\nFalse")

if item.searchItem("Harvard University"):
    print("\nTrue")
else:
    print("\nFalse")

if item.searchItem("Boston University"):
    print("\nTrue")
else:
    print("\nFalse\n")