import math

a = int(input("a sonni kiriting: "))
b = int(input("b sonni kiriting: "))
c = int(input("c sonni kiriting: "))

if a!=0:
    d=math.sqrt(b**2-4*a*c)
    x1=( (-1)*b + d)/2*a
    x2=( (-1)*b - d)/2*a
    r = (x1!=0 and x2!=0)
    print(r,"\n",x1,"\n",x2,"\n")