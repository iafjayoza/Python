class Node:
    def __init__(self, v = None):
        self.value = v
        self.next = None
        return

    def isempty(self):
        return (self.value == None)

    def append(self,v):
        if self.isempty():
            self.value = v
            return
        tmp = self
        while tmp.next != None:
            tmp = tmp.next
        newnode = Node(v)
        tmp.next = newnode
        return

    def insert(self,v):
        if self.isempty():
            self.value = v
            return

        newnode = Node(v)
        (self.value,newnode.value) = (newnode.value,self.value)
        (self.next,newnode.next) = (newnode,self.next)
        return

    def delete(self,v):
        if self.isempty():
            return
        if self.value == v:
            if self.next == None:
                self.value = None
            else:
                self.value = self.next.value
                self.next = self.next.next
                return
        tmp = self
        while tmp.next != None:
            if tmp.next.value == v:
                tmp.next = tmp.next.next
                return
            else:
                tmp = tmp.next
        return

    def __str__(self):
        selflist = []
        if self.value == None:
            return (str(selflist))

        tmp = self
        selflist.append(tmp.value)

        while tmp.next != None:
            tmp = tmp.next
            selflist.append(tmp.value)
        return (str(selflist))

l = Node(0)
print(l)

for i in range(1,11):
    l.append(i)
print(l)

l.delete(4)
print(l)

l.insert(4)
print(l)

for i in range(10):
    l.delete(i)

print(l)




