
class Node:
    def __init__(self,v):
        self.value = v
        self.next = None
        return

class Linkedlist:
    def __init__(self):
        self.head = None

    def insert(self, v):
        newnode = Node(v)
        newnode.next = self.head
        self.head = newnode

    # Utility function to print it the linked LinkedList
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.value),
            temp = temp.next

    # def detectLoop(self):
    #     s = set()
    #     tmp = self.head
    #
    #     while(tmp):
    #         if tmp in s:
    #             return True
    #         else:
    #             s.add(tmp)
    #             tmp = tmp.next
    #     return False

    def detectLoop(self):
        slow_p = self.head
        fast_p = self.head
        while (slow_p and fast_p and fast_p.next):
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            if slow_p == fast_p:
                return True
        return False

l = Linkedlist()
l.insert(5)
l.insert(4)
l.insert(3)
l.insert(2)
l.insert(1)
l.printList()

l.head.next.next.next.next.next = l.head


if l.detectLoop():
    print("Detected loop")
else:
    print("No loop")



