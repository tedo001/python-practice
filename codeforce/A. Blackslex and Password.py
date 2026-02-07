size=int(input("enter a size of a array:"))
for i in range(size):
    if i==0:
        q=str(input("enter the 1st value:"))
        num=0
        for u in q:
            num=num+int(u)
        continue
    elif i==1:
        o=str(input("enter the 2nd value:"))
        num1=0
        for f in o:
            num1=num1+int(f)
        continue
    else:
        h=str(input("enter the 3rd value:"))
        num2=0
        for l in h:
            num2=num2+int(l)
        break
print(num+1)
print(num1+1)
print(num2+1)