class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Btree:
    def __init__(self):
        self.root = None

    def add(self, data):
        if self.root is None:
            self.root = Node(data)
            return
        self._add(self.root, data)

    def _add(self, root, data):
        if data < root.data:
            if root.left is None:
                root.left = Node(data)
            else:
                self._add(root.left, data)

        else:
            if root.right is None:
                root.right = Node(data)
            else:
                self._add(root.right, data)

    def printBTree(self, root):
        if root:
            self.printBTree(root.left)
            print(root.data, end=' ' if root else '')
            self.printBTree(root.right)


bt = Btree()
bt.add(20)
bt.add(25)
bt.add(15)
bt.add(30)
bt.add(10)
bt.add(45)
bt.add(5)

bt.printBTree(bt.root)
