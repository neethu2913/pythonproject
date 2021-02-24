class emp:
    def __init__(self,eid,name,desig,sal,exp):
        self.eid=eid
        self.name=name
        self.desig=desig
        self.sal=sal
        self.exp=exp
    def __str__(self):
        return self.sal

f=open("employee","r")
employee=[]
for line in f:
  eid,name,desig,sal,exp=line.rstrip("\n").split(",")
  employee.append(emp(eid,name,desig,sal,exp))


sal=[]
for num in employee:
    sal.append(num.sal)
print(max(sal))

