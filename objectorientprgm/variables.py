class employee:
    company_name="aaa"
    def __init__(self,name,age):# init is a constructor,Constructors are used to initialize the object’s state.
        self.name=name
        self.age=age

    def print_person(self):
        print(self.name)
        print(self.age)
        print(employee.company_name)
emp=employee("abi",20)
print(emp.name)
print(employee.company_name)