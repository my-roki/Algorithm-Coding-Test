import sys


def is_surprising(N):
    for i in range(1, len(N) - 1):
        buckets = set()
        for j in range(len(N) - i):
            buckets.add(N[j] + N[j + i])
            if len(buckets) != j + 1:
                return False
    return True


N = sys.stdin.readline().rstrip()
while N != "*":
    if is_surprising(N):
        print(N, "is surprising.")
    else:
        print(N, "is NOT surprising.")

    N = sys.stdin.readline().rstrip()
