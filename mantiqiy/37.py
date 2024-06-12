
x1 = int(input("x1 sonni kiriting: "))
y1 = int(input("y1 sonni kiriting: "))

x2 = int(input("x2 sonni kiriting: "))
y2 = int(input("y2 sonni kiriting: "))

resultx = (x1-1 <= x2) or (x2 <= x1 +1)
resulty = (y1-1 <= y2) or (y2 <= x2+1 )
r=resultx and resulty
print(r)