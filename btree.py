class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


class BTree:
    def __init__(self):
        self.root = None

    def add(self, val):
        if self.root is None:
            self.root = Node(val)

        else:
            self._add(self.root, val)

    def _add(self, root, val):
        if val < root.data:
            if root.left is None:
                root.left = Node(val)
            else:
                self._add(root.left, val)
        else:
            if val > root.data:
                if root.right is None:
                    root.right = Node(val)
                else:
                    self._add(root.right, val)

    def printBT(self, root):
        if root:
            self.printBT(root.left)
            print(root.data, end=' ')
            self.printBT(root.right)


bt = BTree()
bt.add(5)
bt.add(10)
bt.add(7)
bt.add(2)
bt.add(3)
bt.add(1)
bt.add(52)
bt.add(48)
bt.add(12)
bt.add(8)

bt.printBT(bt.root)
