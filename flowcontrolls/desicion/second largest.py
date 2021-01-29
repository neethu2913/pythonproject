num1=int(input("enter the num1"))
num2=int(input("enter the num2"))
num3=int(input("enter the num3"))

if(num1<num2)&(num1>num3):
    if(num2>num3):
        print (num2,"is the sec largest")
    else:
        print(num3,"is the  sec largest")

if(num2>num1)&(num2>num3):
    if(num1>num3):
        print(num1,"is the sec largest")
    else:
        print(num3,"is the sec largest")

if(num3>num2)&(num3>num1):
    if(num2>num1):
        print(num2,"is sec largest")
    else:
        print(num1,"is sec largest")

