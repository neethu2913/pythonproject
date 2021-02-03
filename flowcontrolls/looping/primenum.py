num=int(input("enter the num"))#9
flg=0
for i in range(2,num):#(2,8
    if(num%i==0):#9%2==0
        flg=1
        break
    else:
        flg=0
if(flg==0):
    print("prime")
else:
    print("not prime")


