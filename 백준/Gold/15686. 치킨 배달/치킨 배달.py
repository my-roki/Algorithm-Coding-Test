import sys
from itertools import combinations


def input():
    return sys.stdin.readline().strip()


def get_distance(a: tuple, b: tuple):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


if __name__ == "__main__":
    N, M = map(int, input().split())

    homes = []
    all_chickens = []
    for i in range(N):
        row = input().split()
        for j in range(len(row)):
            cdt = row[j]
            if cdt == "2":
                all_chickens.append((i, j))
            elif cdt == "1":
                homes.append((i, j))

    not_closed = combinations(all_chickens, M)
    answer = sys.maxsize
    for nc in not_closed:
        total_home2chicken = 0
        for home in homes:
            min_distance = sys.maxsize
            for chicken in nc:
                min_distance = min(min_distance, get_distance(home, chicken))
            total_home2chicken += min_distance

        answer = min(answer, total_home2chicken)

    print(answer)