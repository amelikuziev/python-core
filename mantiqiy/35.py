x1 = int(input("x1 sonni kiriting: "))
x2 = int(input("x2 sonni kiriting: "))
y1 = int(input("y1 sonni kiriting: "))
y2 = int(input("y2 sonni kiriting: "))

if x1%2==1 and y1%2==1 or x1%2==0 and y1%2==0:
    r1 = "qora"
else:
    r1 = "oq"

if x2%2==1 and y2%2==1 or x2%2==0 and y2%2==0:
    r2 = "qora"
else:
    r2 = "oq"

if r1 == r2:
    print(f"ular bir xil {r2} rangda.")