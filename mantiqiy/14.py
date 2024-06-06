a = int(input("a sonni kiriting: "))
b = int(input("b sonni kiriting: "))
c = int(input("c sonni kiriting: "))

r = a>0 and b<0 and c<0 or a<0 and b>0 and c<0 or a<0 and b<0 and c>0
print(r)