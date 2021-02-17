f=open("words","r")
lst=[]
for line in f:
   #for word in line.rstrip("\word):
   #for word in line.split
   words=line.strip("\n").split(" ")
   for word in words:
       lst.append(word)
for word in lst:
        print(word)
