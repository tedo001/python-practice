size=int(input())
m=[]
n=[]
j=[]
for i in range(size):
    if i==0:
        m.append(int(input()))
        continue
    elif i==1:
        n.append(int(input()))
    else:
        j.append(int(input()))



n.append(int(input()))
j.append(int(input()))
m2=m[0]*m[1]
n2=n[0]*n[1]
j2=j[0]*j[1]
print(m2,n2,j2)
