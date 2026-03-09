t = int(input())          # fix 1: read t
for _ in range(t):        # fix 2: loop over test cases
    n = int(input())      # fix 3: read n
    a = list(map(int, input().split()))   # fix 4: .split() to parse integers
    M = max(a)
    m = []
    count = 0
    for i in range(n):
        if a[i] == M:
            continue
        else:
            m.append(a[i])    # fix 5: append instead of insert(i,...)
    m.insert(0, M)
    for l in range(n):
        count = M + count
    print(count)