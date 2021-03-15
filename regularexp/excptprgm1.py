lst=[10,20,30,40]
pos=int(input("enter pos"))
try:
    print(lst[pos])
except Exception as e:
    print(e.args)
    #print("exception occured")