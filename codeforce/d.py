size=int(input())
h="yes"
n="no"
for i in range(size):
    a,b,c,d=str(input())
    if a==b==c==d:
        return h
    else:
        return n