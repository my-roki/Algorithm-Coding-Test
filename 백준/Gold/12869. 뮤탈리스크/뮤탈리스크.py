import sys
from collections import deque
from itertools import permutations


def input():
    return sys.stdin.readline().strip()


def bfs(a: int, b: int, c: int) -> int:
    q.append((a, b, c))
    visited[a][b][c] = 1

    while q:
        a, b, c = q.popleft()
        if a == 0 and b == 0 and c == 0:
            return visited[a][b][c]
        for da, db, dc in permutations([9, 3, 1], 3):
            na = max(0, a - da)
            nb = max(0, b - db)
            nc = max(0, c - dc)
            if visited[na][nb][nc] != 0:
                continue

            visited[na][nb][nc] = visited[a][b][c] + 1
            q.append((na, nb, nc))

    return visited[0][0][0]


if __name__ == "__main__":
    N = int(input())
    scv = list(map(int, input().split()))
    scv += [0] * (3 - N)  # scv가 3마리 보다 적을 경우
    visited = [[[0] * 61 for _ in range(61)] for _ in range(61)]
    q = deque()

    print(bfs(scv[0], scv[1], scv[2]) - 1)