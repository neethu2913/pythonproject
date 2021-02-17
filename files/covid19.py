f=open("covid_19","r")
dict={}
for line in f:
    data=line.rstrip("\n").split(",")
    state=data[3]
    confrimed_case=int(data[-1])

    dict[state]=confrimed_case

for k,v in dict.items():
  print(k,"===",v)

data=max(dict,key=dict.get)
print(data)# print(data)nameofplace
#print (dict[data])=num
