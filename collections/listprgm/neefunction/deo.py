#def add(*args):
    #total=0
   # for num in args:
  #    total+=num
 #   print(total)
#add(10,20,30,40,50)#150


def print_emp_data(**args):#dictinry format  #(*args):#tuple
   for k,v in args.items():
       print(k,v)

print_emp_data(eid=100,job="kakkanad" ,home="idukki") #dict   #tuple:(100,kakkanad,thirussr)