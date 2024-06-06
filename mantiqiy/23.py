a = int(input("a sonini kiriting: "))

birlar = a%10
onlar = (a-birlar)//10%10
yuzlar = (a-birlar- onlar*10)//100
r = (birlar==yuzlar and onlar!=yuzlar )
print(r)
