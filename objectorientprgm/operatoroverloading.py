class book:
    def __init__(self,pages):
        self.pages=pages

    def __add__(self, other):
        return book(self.pages+other.pages)

    def __sub__(self, other):
        return book(self.pages-other.pages)

    def __str__(self):
        return str(self.pages) #str(self.pages) =int convert to string/ (return self.page) =eroor occur  $int val
obj=book(100)
obj1=book(200)
obj2=book(150)

#print(obj+obj1)#int  (add method) #300
#print(obj-obj1)
print(obj+obj1+obj2) #obj+obj1=int ,obj2=book type (so return str = )obj+obj1+obj2=str
print(obj+obj1-obj2)




#__add__= +
#__sub__ = -
#__truediv__ =/
#__mul__= *
