import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())
cards = map(int, sys.stdin.readline().split())

c = combinations(cards, 3)
result = 0
for i in c:
    c_sum = sum(i)
    if c_sum > M:
        continue
    elif c_sum == M:
        print(M)
        quit()
    else:
        result = max(result, c_sum)
print(result)