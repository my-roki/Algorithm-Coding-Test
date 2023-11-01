import sys


def go(a: int, b: int, c: int) -> int:
    if b == 1:
        return a % c

    temp = go(a, b // 2, c)
    if b % 2 == 1:
        return temp * temp * a % c
    else:
        return temp * temp % c


if __name__ == "__main__":
    A, B, C = map(int, sys.stdin.readline().split())

    print(go(A, B, C))
