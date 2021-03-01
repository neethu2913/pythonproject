employees=[
    {"name":"varun","design":"develop","salary":34000,"join":1999,"resign":2001},
    {"name":"anu","design":"develop","salary":30000,"join":1992,"resign":2002},
    {"name":"ram","design":"qa","salary":40000,"join":2004,"resign":2005},
    {"name":"raju","design":"qa","salary":33300,"join":2005,"resign":2017},
    {"name":"sruthi","design":"design","salary":29000,"join":2002,"resign":2009}
]

highestsal=max(list(map(lambda emp:emp["salary"],employees)))
print((highestsal))

higemp=list(filter(lambda emp:emp["salary"]==highestsal,employees))
print(higemp)

exp=list(filter(lambda emp:emp["resign"]-emp["join"]>8,employees))
print(exp)

