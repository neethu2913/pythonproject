f=open("filedemo","r")
lst=[]
for line in f:
    print(line)

    lst.append(line.rstrip("\n"))
print(lst)