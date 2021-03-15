from re import *
f=open("dob","r")

rule="[0-9]{2}\/[0-9]{2}\/[0-9]{4}"
lst=[]

for date in f:
    date=date.rstrip("\n")
    print(date)
    match=fullmatch(rule,date)
    if match!=None:
       lst.append(date)
print(lst)



