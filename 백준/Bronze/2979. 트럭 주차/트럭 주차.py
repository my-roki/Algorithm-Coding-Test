import sys


A, B, C = map(int, sys.stdin.readline().rstrip().split())

parking = [0] * 100
for k in range(3):
    start, end = map(int, sys.stdin.readline().split())

    for j in range(start - 1, end - 1):
        parking[j] += 1

result = 0
for k in parking:
    if k == 1:
        result += k * A
    if k == 2:
        result += k * B
    if k == 3:
        result += k * C
print(result)