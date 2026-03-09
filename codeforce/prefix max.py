a=list(input())
size=len(a)
M=max(a)
m=[]
count=0
for i in range(size):
      if a[i]==M:
          continue
      else:
          m.insert(i,a[i])
m.insert(0,M)
for l in range(size):
    count=M+count
print(count)

