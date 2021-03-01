from re import *

pattern="ab"
source="ababaaabbabab"
matcher=finditer(pattern,source)
count=0
for mat in matcher:
    print(mat.start())
    print(mat.group())
    count+=1
print(count)