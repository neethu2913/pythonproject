lst1=[1,2,3]
lst2=[2,4,5]
#lst=[]
#for i in lst1:
#    for j in lst2:
#       lst.append((i,j))
#print(lst)

lst=[(i,j)for i in lst1 for j in lst2]
print(lst)

lst=[i**2for i in lst1]
print(lst)

lst=[i**3for i in lst2]
print(lst)

lst=[(j,i)for j in lst2 for i in lst1]
print(lst)

lst=[i for i in lst1 if i%2==0]
print(lst)

lst=[(i,j) for i in lst1 for j in lst2 if i==j]
print(lst)