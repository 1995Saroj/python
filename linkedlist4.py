# This is a python program
# to access a specific item
# in a singly linked list
# using an index value

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
    
    def appendItem(self, data):
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

    def __getitem__(self, index):
        if index > self.count - 1:
            return "Out of Range"
        current = self.tail
        for n in range(index):
            current = current.next
        return current.data

item = linkedList()

item.appendItem("Standford University")
item.appendItem("Harvard University")
item.appendItem("Boston University")

for i in item.iterateItem():
    print(i)
    
print("\nSearch the Index: ")

print("\n",item[1])
print("\n",item[2])
print("\n",item[5])
