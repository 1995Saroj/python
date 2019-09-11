# This is a binary search tree algorithm to insert and print the elements in the binary search tree and I'm still working on it

class Node:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, current):
        if data < current.data:
            if current.leftChild == None:
                current.leftChild = Node(data)
            else:
                self._insert(data.current.leftChild)
        elif value > current.data
            if current.rightChild == None:
                current.rightChild = Node(data)
            else:
                self._insert(data, current.rightChild)
        else:
            print("The value already exists in the tree.")
    def printTree(self):
        if self.root != None:
            self._printTree(self.root)
    
    def _printTree(self, current):
        if current != None:
            self._printTree(current.leftChild)
            print str(current.data)
            self._printTree(current.rightChild)

        



