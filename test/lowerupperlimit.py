num=int(input("enter the num"))
low=int(input("enter the low range"))
upper=int(input("enter the upper range"))

for i in range(1,(upper+1)):
    if i**num in range(low,upper+1):
      print(i**num)
