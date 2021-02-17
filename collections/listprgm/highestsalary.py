employees=[
    [100,"tom","developer",23000],
    [200,"john","hr",13000],
    [340,"sruthi","ba",24000],
    [240,"vidhya","developer",25000]
]

sallist=[]
for emp in employees:
    sallist.append(emp[3])
print("high salary=",max(sallist))