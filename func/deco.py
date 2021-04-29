def my_div(func):#2,10
    def innerfun(num1,num2):#2,10
        if num1<num2:#2<10
            num1,num2=num2,num1#10,2
        return func(num1,num2)#div(10,2)
    return innerfun

@my_div

def div(num1,num2):

    return(num1/num2)

print(div(2,10))