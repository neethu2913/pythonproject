pattern="ABABC"
dict={}
for char in pattern:
    if char not in dict:
        dict[char]=1
    else:
        print(char,"is first recursive")
        break