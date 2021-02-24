employee={
    1000:{"eid":1000,"ename":"neethu","desig":"developer","sal":34500},
    1002:{"eid":1002,"ename":"nandhu","desig":"hr","sal":34500},
    1003:{"eid":1003,"ename":"sruthi","desig":"developer","sal":23500}
}
#eid=int(input("enter the eid"))
#property=input("enter the property")
#if eid in employee:
 #   print(employee[eid]["ename"])
 #  if property in employee[eid]:
#     print(employee[eid][property])
 #  else:
#        print("invalid property")
#
#else:
#   print("invalid eid")

def print_employee_details(**kwargs):#dict
  id=kwargs["eid"]

  if id in employee:
    print(employee[id]["ename"])
    prop=kwargs["property"]
    print(employee[id][prop])
  else:
    print("id not exist")

print_employee_details(eid=1002,property="desig")
