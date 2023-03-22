import sys

h, m = map(int, sys.stdin.readline().split())

if m < 45 and h != 0:
    print(h - 1, 15 + m)
elif m < 45 and h == 0:
    print(23, 15 + m)
else:
    print(h, m - 45)
