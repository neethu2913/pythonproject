#single inheritance
class parent:
    def phone(self):
        print("inside parents phone method")
class child(parent):
    pass
ch=child()
ch.phone()
#multilevel inheritance
class parent:
    def m1(self):
        print("inside m1")
class subchild(parent):
    def m2(self):
        print("inside m2")
class child(subchild):
    def m3(self):
        print("inside m3")
ch=child()
ch.m1()
ch.m2()
ch.m3()

#mulitple inheritance
class parent:
    def m1(self):
        print("m1")
class subchild:
    def m2(self):
        print("m2")
class child(subchild,parent):
    def m3(self):
        print("m3")
ch=child()
ch.m1()
ch.m2()
ch.m3()