# Class  example of fruits

class Fruits:
    def __init__(self,name,color,test,price):
        self.name = name
        self.color = color
        self.test = test
        self.price = price

    def iscostly(self):
        if self.price > 100:
            return "{} is costly".format(self.name)
        else:
            return "{} is not costly".format(self.name)


fruit1 = Fruits("Mango","Yellow","Sweet",140)
fruit2 = Fruits("Orange","Green","Tangy",40)
fruit3 = Fruits("Apple","Red","Sweet",180)

print(fruit1.name,fruit1.color,fruit1.test,fruit1.price,fruit1.iscostly())
print(fruit2.name,fruit2.color,fruit2.test,fruit2.price,fruit2.iscostly())
print(fruit3.name,fruit3.color,fruit3.test,fruit3.price,fruit3.iscostly())