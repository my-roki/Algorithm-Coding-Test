import sys


if __name__ == "__main__":
    N, C = map(int, sys.stdin.readline().strip().split())
    arr = sys.stdin.readline().strip().split()
    d = {}  # key=번호, value=[위치, 개수]

    for idx, i in enumerate(arr):
        if i in d:
            d[i][1] += 1
        else:
            d[i] = [idx, 1]

    numbers = [[i, j] for i, j in d.items()]
    numbers.sort(key=lambda x: (-x[1][1], x[1][0]))

    result = ""
    for i, j in numbers:
        result += f"{i} " * j[1]

    print(result[:-1])