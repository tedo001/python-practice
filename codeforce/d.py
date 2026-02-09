t = int(input())

for j in range(t):
    a, b, c, d = map(int,input().split())
    if a == b == c == d:
        print("YES")
    else:
        print("NO")
