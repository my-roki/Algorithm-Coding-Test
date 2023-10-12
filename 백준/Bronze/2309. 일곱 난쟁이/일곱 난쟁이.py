import sys
from itertools import combinations

N = 9
arr = []
for i in range(N):
    arr.append(int(sys.stdin.readline().rstrip()))

for i in combinations(arr, 7):
    if sum(i) == 100:
        i = sorted(i)
        for j in i:
            print(j)
        break
