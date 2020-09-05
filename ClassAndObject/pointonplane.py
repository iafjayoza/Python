from math import *
class Point:
    def __init__(self,a=0,b=0):
        self.x = a
        self.y = b

    def translate(self,deltax,deltay):
        self.x += deltax
        self.y += deltay

    def odistance(self):
        print("Distance from origin is",sqrt((self.x*self.x)+(self.y *self.y)))
        return (sqrt((self.x*self.x)+(self.y *self.y)))

p = Point(1,1)
p.translate(2,3)
p.odistance()
print(p.x,p.y)

q = Point()
q.translate(2,3)
q.odistance()
print(q.x,q.y)