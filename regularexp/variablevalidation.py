from re import *

#rule="[a-kA-K][369][a-zA-Z0-9]"
#rule="[K][L][0-9]{2}[A-Z]{2}[0-9]{1,4}"
#rule='\w{1,64}@gmail.com'
#rule="\d{10}"

variablename=input("enter variable name")

mat=fullmatch(rule,variablename)
if mat!=None:
    print("valid variable name")
else:
    print("invalid")

