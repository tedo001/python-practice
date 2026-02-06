size=str(input())
m=[]
n=[]
j=[]
for i in range(len(size)):
    print(i)
    if i==0:
        q=int(input())
        m.append(q)
        continue
    elif i==1:
        o=str(input())
        n.append(o[0]+o[1])
        print(n)
        continue
    else:
        h=(input())
        j.append(h)
        break
m2=[]
m2.append(m[0*1]+1)
print(m2)
