no1=int(input("enter the no1"))
no2=int(input("enter the no2"))
try:
    res=no1/no2
    print(res)
except:
    no2 = int(input("enter the no2"))
    res=no1/no2
    print(res)
finally:
    print("data base op")
    print("file write")