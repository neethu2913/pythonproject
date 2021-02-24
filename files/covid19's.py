f=open("covid_19","r")
dict={}
lst=[]
for line in f:
    data={'state':{'state:','confrimed_case:']}
    line.rstrip('\n').split(",")
    state=data[3]
    confrimed_case=[-1]

    dict[state]=confrimed_case
    print(data)