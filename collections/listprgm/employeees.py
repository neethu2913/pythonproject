employees=[
    [170,"hari","developer",23500,1987,2000]
    [136,"vidhya","developer",34000,1976,1999]
    [123,"nandhu","engg",56489,1988,2002]
    [345,"neethu","designer",12345,1987,2001]
]
totsal=0
for emp in employees:
    print(emp[1])

for emp in employees:
    if emp[2]=="developer":
        print(emp[2])

for emp in employees:
    totsal++emp[3]
print(totsal)