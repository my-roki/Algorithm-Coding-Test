import sys


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    [prev, last] = sys.stdin.readline().rstrip().split("*")

    for _ in range(N):
        candidate = sys.stdin.readline().strip()
        if len(candidate) < len(prev) + len(last):
            print("NE")
            continue

        if candidate[0 : len(prev)] == prev and candidate[-len(last) :] == last:
            print("DA")
        else:
            print("NE")
