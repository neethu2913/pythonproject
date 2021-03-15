
num =int(input("enter the num"))
try:
    if num<0:
        raise Exception("invalid num")
except Exception as e:
    print(e.args)