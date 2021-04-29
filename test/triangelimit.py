#rows=5
for row in range(0,6):
   for col in range(0,10):
     if(row==5)|(col+row==6)|(col-row==4):
         col="*"
         print("*",end="")
   else:
    print(" ",end="")
print("")
#rows = 5

#for i in range(0, rows):

#    for j in range(0, i + 1):
#        print("*", end=' ' )
 #       print("\r")