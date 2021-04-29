def dec(func):
    def inner(phno):
        if len(phno)>10:
            raise Exception("inalid")
        else:
            return func(phno)
    return inner
@dec
def valphn(phno):
    return"valid"+phno
print(valphn("1234567890"))