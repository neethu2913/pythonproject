#filter
lst=[1,2,3,4,5,6,7,8,9]

even=list(filter(lambda no:no%2==0,lst))
print(even)

grt=list(filter(lambda no:no>3,lst))
print(grt)