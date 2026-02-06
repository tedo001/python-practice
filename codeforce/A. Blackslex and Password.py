size=str(input())
m=[]
n=[]
j=[]
for i in range(len(size)):
    if i==0:
        q=int(input())
        m.append(q)
        continue
    elif i==1:
        o=int(input())
        n.append(o)
        continue
    else:
        h=(input())
        j.append(h)
        break
m2=m[0]*m[1]+1
n2=n[0]*n[1]+1
j2=j[0]*j[1]+1
print(m2,n2,j2)
