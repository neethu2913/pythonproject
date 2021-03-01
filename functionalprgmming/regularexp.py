from re import *

#pattern='[ab]'  #either a or b
#pattern='[a-z]' # checking for alphabets lower case
#pattern='[A-Z]'  #upper case alphabets
#pattern='[a-zA-Z]' #both upper and lower alphabets
#pattern='[0-9]' # digits
#pattern='[a-zA-Z0-9]' #upper,lower alphabets,digits
#pattern='[^0-9]'  #expext 0-9
#pattern='[^a-zA-Z0-9]' #expect alphabets,digits
#pattern="\s"   #space
#pattern="\d"  #[0-9]
#pattern="\D"  #[^0-9]  #expect digits
#pattern="\w" #all words [a-zA-z0-9_#]
pattern="\W"  #_ not taken

source="ab Zk@ok1_#$%&*!"
matcher=finditer(pattern,source)
count=0
for mat in matcher:
    print(mat.start())
    print(mat.group())
    count+=1
print(count)