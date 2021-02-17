arr1=[10,11,12,13]
arr2=[10,12,16,25]
res=[]
for i in arr1:
    for j in arr2:
        if i==j:
            res.append(i)
print(res)