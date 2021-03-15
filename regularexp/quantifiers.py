from re import *


#pattern="a+"  #chk for one or morethan a
#pattern="a*"   #a++ zero number of a cont a the postion of b
#pattern="a{2}"   # max two number of a's
pattern="a{2,3}"  #min two,max three
matcher=finditer(pattern,"aaabaabaaab")

for mat in matcher:
    print(mat.start())
    print(mat.group())