a = int(input("a sonni kiriting: "))
b = int(input("b sonni kiriting: "))

r = a%2==1 and b%2==1 or a%2==0 and b%2==0
print(r)