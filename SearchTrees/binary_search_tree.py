class Tree:
    #Empty node has self.value, self.left and self.right all None
    #Leaf has self.value != None and self.left and self.right to point to empty node
    def __init__(self,initval=None):
        self.value = initval
        if self.value:
            self.left = Tree()
            self.right = Tree()
        else:
            self.left = None
            self.right = None
        return

    #Only empty node has value none
    def isempty(self):
        return (self.value == None)

    #Leaf node have both childer empty
    def isleaf(self):
        return (self.left.isempty() and self.right.isempty())

    #Convert a leaf node to an empty node
    def makeempty(self):
        self.value = None
        self.left = None
        self.right = None
        return

    #Copy right child value to current node
    def copyright(self):
        self.value = self.right.value
        self.left = self.right.left
        self.right = self.right.right
        return

    #Check if value v occurs in tree
    def find(self,v):
        if self.isempty():
            print("False")
            return (False)
        if self.value == v:
            print("True")
            return (True)
        if v < self.value:
            return (self.left.find(v))
        if v > self.value:
            return (self.right.find(v))

    #Insert value v in tree
    def insert(self,v):
        if self.isempty():
            self.value = v
            self.left = Tree()
            self.right = Tree()

        if self.value == v:
            return

        if v < self.value:
            self.left.insert(v)
            return
        if v > self.value:
            self.right.insert(v)
            return

    #Find maximum value in non empty tree
    def maxval(self):
        if self.right.isempty():
            return (self.value)
        else:
            return (self.right.maxval())

    #Delete value V from tree
    def delete(self,v):
        if self.isempty():
            return
        if v < self.value:
            self.left.delete(v)
            return
        if v > self.value:
            self.right.delete(v)
            return

        if v == self.value:
            if self.isleaf():
                self.makeempty()
            elif self.left.isempty():
                self.copyright()
            else:
                self.value = self.left.maxval()
                self.left.delete(self.left.maxval())
            return

    #Inorder Traversal
    def inorder(self):
        if self.isempty():
            return ([])
        else:
            return (self.left.inorder()+[self.value]+self.right.inorder())

    #Display tree as a string
    def __str__(self):
        return (str(self.inorder()))

t = Tree()

for i in [1,34,2,23,4,54,3,8,0,9]:
    t.insert(i)
print(t)

t.insert(55)
print(t)

t.insert(4.5)
print(t)

t.delete(54)
print(t)

t.find(55)
t.find(111)