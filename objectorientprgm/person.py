class person:
    def __init__(self,age,name):
        self.age=age
        self.name=name
p1=person(27,"ram")
p2=person(23,"abi")
p3=person(29,"nandhu")
employees=[]
employees.append(p1)
employees.append(p2)
employees.append(p3)
age=[]
for emp in employees:
    age.append(emp.age)
print(max(age))