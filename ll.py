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

    def printLL(self):
        if self.head is None:
            print('LinkedList is empty')
            return
        temp = self.head
        while temp:
            print(temp.data, end='->' if temp.next else '')
            temp = temp.next

    def remove(self, key):
        if self.head is None:
            print('LinkedList is empty')
            return
        if self.head.data == key:
            self.head = self.head.next
        else:
            temp = self.head
            prev = None
            while temp:
                if temp.data == key:
                    if prev:
                        prev.next = temp.next
                    return
                prev = temp
                temp = temp.next

            print('key not found')


ll = LinkedList()
ll.add(5)
ll.add(10)
ll.add(15)
ll.add(20)
ll.add(25)
ll.add(30)
ll.add(35)

ll.printLL()

ll.remove(15)
print()

ll.printLL()
