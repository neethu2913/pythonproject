iplpoints=[ {"team": "csk", "mp":6, "won":5, "los":1,"pts":10},
               {"team":"srh","mp":6, "won":1,"los":5,"pts":2},
               {"team":"rcb", "mp":6, "won":5, "los":1,"pts":10},
               {"team": "csk","mp":6, "won":5, "los":1,"pts":10},
               {"team": "rr","mp":5,"won":2,"los":3,"pts":4},
               {"team": "dc", "mp":6,"won":4,"los":2,"pts":8},
               {"team": "pbks","mp":6, "won":2,"los":4, "pts":4}
            ]
#count


#sorted
iplpoints.sort(key=lambda item: item.get("pts"))               
print(iplpoints)
#team name in uppercase
name=list(map(lambda dict:dict["team"].upper(),iplpoints))
print(name)

#highest point
highestpoint=max(list(map(lambda dict:dict["pts"],iplpoints)))
print((highestpoint))
#lowest point
lowestpoint=min(list(map(lambda dict:dict["pts"],iplpoints)))
print(lowestpoint)