size=int(input())
h="yes"
n="no"
for i in range(size):
    a,b,c,d=str(input())
    if a==b==c==d:
        h="yes"
    else:
        r="no"
print(h)
print(n)