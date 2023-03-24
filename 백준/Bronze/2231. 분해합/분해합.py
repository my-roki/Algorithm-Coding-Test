import sys

N = int(sys.stdin.readline().rstrip())

for i in range(1, N + 1):
    constructor = i + sum(map(int, str(i)))
    if constructor == N:
        print(i)
        quit()
print(0)