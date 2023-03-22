import sys

TC = int(input().rstrip())

cnt = 0
for _ in range(TC):
    N = sys.stdin.readline().rstrip()
    for i in range(1, len(N)):
        if N[i - 1] != N[i] and N[i] in N[0:i]:
            break
    else:
        cnt += 1
print(cnt)
