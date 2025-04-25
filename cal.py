                     # calculator

a=int(input("enter a: "))
b=int(input("enter b: "))
c=int(input("enter operator(+,-,*,%,/)(1 to 5):"))                   
if c==1:
    print(a+b)
elif c==2:
   print(a-b)
elif c==3:
   print(a*b)
elif c==4:
   print(a%b)
elif c==5:
    if b==0:
       print("error because division by 0 is not allowed")
    else:
       print(a/b)
else:
   print("invalid operator")



