class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = newNode

    def swap(self):
        currentNode = self.head
        self.head = currentNode.next
        prev = None
        while currentNode and currentNode.next:
            nextNode = currentNode.next
            next2Next = nextNode.next
            nextNode.next = currentNode
            if prev:
                prev.next = nextNode

            currentNode.next = next2Next
            prev = currentNode
            currentNode = next2Next

    def printLL(self):
        temp = self.head
        while temp:
            print(temp.data, end='->' if temp.next else '')
            temp = temp.next


ll = LinkedList()
ll.add(1)
ll.add(2)
ll.add(3)
ll.add(4)

ll.printLL()
print()
ll.swap()

ll.printLL()
