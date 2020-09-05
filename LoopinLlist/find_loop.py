# program to find a loop in linked list
class Node:
    def __init__(self, v):
        self.value = v
        self.next = None
        return

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self,v):
        newnode = Node(v)
        newnode.next = self.head
        self.head = newnode

    def printlist(self):
        tmp = self.head
        while(tmp):
            print(tmp.value)
            tmp = tmp.next

    # def findloop(self):
    #     s = set ()
    #     tmp = self.head
    #
    #     while (tmp):
    #         if tmp in s:
    #             return True
    #         else:
    #             s.add(tmp)
    #             tmp = tmp.next
    #     return False

    def findloop(self):
        slow_p = self.head
        fast_p = self.head
        while(slow_p and fast_p and fast_p.next):
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            if slow_p == fast_p:
                return True
        return False

l = LinkedList()
l.insert(10)
l.insert(20)
l.insert(30)
l.insert(40)
l.insert(50)

l.head.next.next.next.next.next = l.head

if l.findloop():
    print("There is a loop")
else:
    print("There is no loop")
