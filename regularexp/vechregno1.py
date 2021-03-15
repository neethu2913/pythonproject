from re import *

rule="[K][L][0-9]{2}[A-Z]{2}[0-9]{1,4}"

f=open("vechregno","r")
lst=[]

for regno in f:
    regno=regno.rstrip("\n")
    print(regno)
    match=fullmatch(rule,regno)
    if match!=None:
      lst.append(regno)
print(lst)


