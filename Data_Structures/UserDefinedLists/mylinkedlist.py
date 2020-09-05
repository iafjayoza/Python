### Linked List ###

class Node:
    def __init__(self, v):
        self.value = v
        self.next = None
        return

    def isempty(self):
        return (self.value == None)

    def append(self, v):
        if self.isempty():
            self.value = v
            return

        tmp = self
        while tmp.next != None:
            tmp = tmp.next
        newnode = Node(v)
        tmp.next = newnode
        return

    def insert(self, v):
        if self.isempty():
            self.value = v
            return

        newnode = Node(v)
        (self.value, newnode.value) = (newnode.value, self.value)
        (self.next,newnode.next) = (newnode, self.next)
        return

    def delete(self, v):
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
        mylist = []

        if self.value == None:
            return (str(mylist))

        tmp = self
        mylist.append(tmp.value)

        while tmp.next != None:
            tmp = tmp.next
            mylist.append(tmp.value)

        return (str(mylist))

l = Node(0)
print(l)

l.append(1)
print(l)

for i in range(10):
    l.append(i)
print(l)

for j in range(3):
    l.insert(j)

print(l)

for i in range(10):
    l.delete(i)


### Queue ###

queuelist = []

def addq(x,v):
    x.insert(0,v)
    print(x)
    return x

def removeq(x):
    x.pop()
    print(x)
    return x

addq(queuelist,1)
addq(queuelist,2)
addq(queuelist,3)
removeq(queuelist)

### Stake ###

mystake = []

def addstake(x,v):
    x.append(v)
    print(x)
    return x

def removestake(x):
    x.pop()
    print(x)
    return x

addstake(mystake,7)
addstake(mystake,8)
addstake(mystake,9)
removestake(mystake)
removestake(mystake)









