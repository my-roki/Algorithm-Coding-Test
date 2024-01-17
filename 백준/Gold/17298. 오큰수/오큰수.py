import sys


def input():
    return sys.stdin.readline().strip()


if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))

    stack = []
    result = [-1] * N
    for idx in range(N):
        while stack and A[stack[-1]] < A[idx]:
            result[stack[-1]] = A[idx]
            stack.pop()
        stack.append(idx)

    print(" ".join(map(str, result)))