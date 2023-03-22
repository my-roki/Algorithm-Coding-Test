import sys

h, m = map(int, sys.stdin.readline().split())
t = int(sys.stdin.readline().rstrip())

if m + t >= 60:
    h += (m + t) // 60
    m = (m + t) % 60
else:
    m += t

if h >= 24:
    h -= 24 

print(h, m)
