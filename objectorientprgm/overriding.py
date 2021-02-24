#class parent:
#   def phone(self):
#       print("have nokia phn")


#class child(parent):
#   def phone(self):
#       print("iphone")

#ch=child()
#ch.phone()

#
class person(object):
    def __init__(self,age,name):
        self.age=age
        self.name=name
    def __str__(self):
        return self.name+str(self.age)

p=person(25,"raj")
p1=person(34,"arun")
print(p)
print(p1)
