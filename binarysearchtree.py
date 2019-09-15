# This is a binary search tree algorithm to insert and print the elements in the binary search tree and I'm still working on it

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)
    
    def _insert(self, data, current):
        if data < current.data:
            if current.left is None:
                current.left = Node(data)
            else:
                self._insert(data, current.left)
        elif data > current.data:
            if current.right is None:
                current.right = Node(data)
            else:
                self._insert(data, current.right)
        else:
            print("The value is already present in the tree.")

    def find(self, data):
        if self.root:
            isFound = self._find(data, self.root)
            if isFound:
                return True
            else:
                return None
        
    def _find(self, data, current):
        if data > current.data and current.right:
            return self._find(data, current.right)
        elif data < current.data and current.left:
            return self.find(data, current.left)
        if data == current.data:
            return True

tree = BinarySearchTree()
tree.insert(10)
tree.insert(7)
tree.insert(11)
tree.insert(17)
tree.insert(1)
tree.insert(19)

print(tree.find(10))
        

