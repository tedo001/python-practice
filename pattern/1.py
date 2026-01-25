num=list(input("enter a shorted num:"))

pivot=num[0]

shorted=[]
for i in range(len(num)):

     if num[i]>pivot:
        shorted.append(num[i])
        print(shorted)
     else:
        print()

        """for n in range(len(num2)):
    if num2[n]>pivot2:
        pivot2=num2[n]
    else:
        num2=pivot2.append(num2[n])"""


