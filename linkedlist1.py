# A python program to apprend and iterate through the linked list

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

    def apprendItem(self, data):
        node = Node(data)
        if self.head:
            self.head.next = node
            self.head = node
        else:
            self.tail = node
            self.head = node
        self.count += 1

item = linkedList()
item.apprendItem("Standford University")
item.apprendItem("Harvard University")
item.apprendItem("Boston University")

for i in item.iterateItem():
    print(i)