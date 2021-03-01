class emp:
    def __init__(self,eid,name,desig,sal,exp):
        self.eid=eid
        self.name=name
        self.desig=desig
        self.sal=int(sal)
        self.exp=int(exp)
    def __str__(self):
        return self.name

f=open("employee","r")
employee=[]
for line in f:
  eid,name,desig,sal,exp=line.rstrip("\n").split(",")
  employee.append(emp(eid,name,desig,sal,exp))

#map(functionalprogramming)
name=list(map(lambda emp:emp.name,employee))
print(name)

#sal=[]
#for num in employee:
#   sal.append(num.sal)

#hw
#print(max(sal))#print employee name whose design ="developer" #filter
#print employee details whose exp >=2 yrs #filter
#print count of employee whose design ="quality analysity"


developer=list(filter(lambda emp:emp.desig=="developer",employee))
name=list(map(lambda emp:emp.name,developer))
print(name)


exp=list(filter(lambda emp:emp.exp>2,employee))
for emp in exp:
 print(emp)


qa=len(list(filter(lambda emp:emp.desig=="qa",employee)))
print(qa)


hisal=min(list(map(lambda emp:emp.sal,employee)))
print(hisal)

