import sys

cnt = 1
while True:
    L, P, V = map(int, sys.stdin.readline().split())
    if L == 0 & P == 0 & V == 0:
        break
    answer = ((V // P) * L) + min((V % P), L)
    print(f"Case {cnt}: {answer}")
    cnt += 1
