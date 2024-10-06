class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.head2 = None
        self.finalListHead = None

    def add1(self, data):
        if self.head is None:
            self.head = Node(data)
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = Node(data)

    def add2(self, data):
        if self.head2 is None:
            self.head2 = Node(data)
            return

        temp = self.head2
        while temp.next:
            temp = temp.next
        temp.next = Node(data)

    def sum(self):
        stack1 = []
        stack2 = []
        if self.head is None and self.head2 is None:
            print('lists are empty')
            return

        if self.head is not None:
            temp = self.head
            while temp:
                stack1.append(temp.data)
                temp = temp.next

        if self.head2 is not None:
            temp = self.head2
            while temp:
                stack2.append(temp.data)
                temp = temp.next
        print(stack1, " ", stack2)
        if stack1 and stack2:
            sum1 = 0
            sum2 = 0
            finalSum = 0
            while stack1:
                sum1 *= 10
                sum1 += stack1.pop()

            while stack2:
                sum2 *= 10
                sum2 += stack2.pop()
            print('sum1', sum1, 'sum2', sum2)

            finalSum = sum1+sum2
            list = []
            while finalSum:
                list.append(finalSum % 10)
                finalSum //= 10
            while list:
                if self.finalListHead is None:
                    self.finalListHead = Node(list.pop(0))
                else:
                    temp = self.finalListHead
                    while temp.next:
                        temp = temp.next
                    temp.next = Node(list.pop(0))

    def printLL1(self):
        if self.head is None:
            print("Linked List is empty")
            return

        current = self.head
        while current:
            print(current.data, end='->' if current.next else '\n')
            current = current.next

    def printLL(self):
        if self.head2 is None:
            print("Linked List is empty")
            return

        current = self.head2
        while current:
            print(current.data, end='->' if current.next else '\n')
            current = current.next

    def printFinalLL(self):
        if self.finalListHead is None:
            print("Linked List is empty")
            return

        current = self.finalListHead
        while current:
            print(current.data, end='->' if current.next else '\n')
            current = current.next


ll = LinkedList()
ll.add1(2)
ll.add1(4)
ll.add1(3)
ll.add2(5)
ll.add2(6)
ll.add2(4)

ll.printLL()
ll.printLL1()

res = ll.sum()
print(res)
ll.printFinalLL()
