import sys

N = sys.stdin.readline().rstrip()
words = ["dz=", "z=", "c=", "c-", "d-", "lj", "nj", "s="]

for i in words:
    N = N.replace(i, "1")
print(len(N))
