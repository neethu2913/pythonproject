num=int(input("enter the num"))

while(num!=0):#123!=0 12!=0
    digit=num%10 #dogot=3 digit=12%10=2 1%10
    print(digit,end="")
    num= num//10
