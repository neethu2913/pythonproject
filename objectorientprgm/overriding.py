#class parent:
#   def phone(self):
#       print("have nokia phn")
#class child(parent):
#   def phone(self):
#       print("iphone")
#ch=child()
#ch.phone()
#the child class a method with the same name of a method in the parent class.

class person(object):
    def __init__(self,age,name):
        self.age=age
        self.name=name
    def __str__(self):
        return self.name+str(self.age)
p=person(25,"raj")
p1=person(34,"annu")
print(p)
print(p1)

# a parent method ca be already implement a child method that are same in the parent. 