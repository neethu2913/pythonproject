players=[
    {"name":"sachin","matches":500,"rank":2},
    {"name":"rohit","matches":450,"rank":12},
    {"name":"sehwag","matches":230,"rank":34},
    {"name":"msd","matches":340,"rank":7}
]
#map
name=list(map(lambda dict:dict["name"],players))
print(name)

rank=list(map(lambda dict:dict["rank"],players))
print(rank)

#filter
#above matche>320
matches=list(filter(lambda dict:dict["matches"]>320,players))
print(matches)



