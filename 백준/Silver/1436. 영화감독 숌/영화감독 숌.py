import sys

for N in sys.stdin.readlines():
    n = 1
    result = 666
    while n < int(N):
        result += 1
        if "666" in str(result):
            n += 1

    print(result)
