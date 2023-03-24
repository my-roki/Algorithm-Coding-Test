import sys

a, b, c, d, e, f = map(int, sys.stdin.readline().split())
print(int((c * e - b * f) / (a * e - b * d)), int((c * d - a * f) / (b * d - a * e)))
