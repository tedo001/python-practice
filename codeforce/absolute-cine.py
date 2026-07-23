
lenth=int(input())
C=[]
D=[]
for i in range(lenth):
    A=list(input())
    for k in range(len(A)):
       J=int(input())
       C.append(J)
    B=list(input())
    for l in range(len(B)):
       N=int(input())
       D.append(N)          

oput=max(C)+D
print(oput)

