ft=open("teams","r")

fd=open("dropped","r")
st=set()
def get_team_set(f):
    st=set()
    for line in f:
       st.add(line.rstrip("\n"))
    return st
st1=get_team_set(ft)
st2=get_team_set(fd)

qualifier=st1-st2
print(qualifier)


#st1=set()
#for line in ft:
#st1.add(line.rstrip("\n"))
#st2=set()

 # for line in fd:
 #st2.add(line.rstrip("/n))

 #qualifier=st1-st2
 # print(qualifier)

