from math import gcd
y, w = map(int, input().split())
wins = 7 - max(y, w)
g = gcd(wins, 6)
print(f"{wins // g}/{6 // g}")