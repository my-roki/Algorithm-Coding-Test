import sys
from typing import List


def print_canvas(canvas: List[List[int]]):
    for i in canvas:
        print(i)
    print("------------")


def dfs(y: int, x: int, h: int):
    visited[y][x] = 1
    for dy, dx in direction:
        ny = dy + y
        nx = dx + x

        if ny < 0 or ny >= N or nx < 0 or nx >= N:
            continue
        if canvas[ny][nx] > h and visited[ny][nx] != 1:
            dfs(ny, nx, h)


if __name__ == "__main__":
    sys.setrecursionlimit(10005)

    N = int(sys.stdin.readline().strip())
    canvas = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    result = 1

    max_h = max(max(i) for i in canvas)
    for h in range(1, max_h + 1):
        cnt = 0
        visited = [[0] * N for _ in range(N)]
        for y in range(N):
            for x in range(N):
                if canvas[y][x] > h and visited[y][x] == 0:
                    dfs(y, x, h)
                    cnt += 1
        result = max(result, cnt)

    print(result)