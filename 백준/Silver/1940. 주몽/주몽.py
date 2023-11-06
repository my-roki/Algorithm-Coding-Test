import sys


if __name__ == "__main__":
    _ = sys.stdin.readline()
    N = int(sys.stdin.readline())
    candidates = sorted(map(int, sys.stdin.readline().split()))

    start, end = 0, len(candidates) - 1
    result = 0
    cnt = 0
    while start < end:
        result = candidates[start] + candidates[end]
        if result > N:
            end -= 1
        elif result < N:
            start += 1
        else:
            cnt += 1
            start += 1
            end -= 1

    print(cnt)
