#lst=[3,4,2,6,7,8]

#lst=[i-1 if i<5 else i+1 for i in lst ]
#print(lst)

lst=[[10,20],[30,40],[50,60]]

lst=[i for ls in lst for i in ls]
print(lst)