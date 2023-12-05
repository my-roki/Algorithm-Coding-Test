import sys
from typing import List


def print_canvas(canvas: List[List[int]]):
    for i in canvas:
        print(i)
    print("------------")


def draw_rectangle(canvas: List[int], ytl: int, xtl: int, ybr: int, xbr: int):
    for y in range(ytl, ybr):
        for x in range(xtl, xbr):
            canvas[y][x] += 1

    return canvas


def dfs(y: int, x: int, r: int) -> int:
    visited[y][x] = 1
    r += 1

    for dy, dx in direction:
        ny = y + dy
        nx = x + dx

        if ny < 0 or ny >= M or nx < 0 or nx >= N:
            continue
        if canvas[ny][nx] == 0 and visited[ny][nx] != 1:
            r = dfs(ny, nx, r)

    return r


if __name__ == "__main__":
    sys.setrecursionlimit(10005)
    M, N, K = map(int, sys.stdin.readline().split())
    canvas = [[0] * N for _ in range(M)]
    visited = [[0] * N for _ in range(M)]
    direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    for _ in range(K):
        xtl, ytl, xbr, ybr = map(int, sys.stdin.readline().split())
        canvas = draw_rectangle(canvas, ytl, xtl, ybr, xbr)

    cnt = 0
    area = []
    for y in range(M):
        for x in range(N):
            if canvas[y][x] == 0 and visited[y][x] == 0:
                r = dfs(y, x, 0)
                area.append(r)
                cnt += 1
    print(cnt)
    print(" ".join(map(str, sorted(area))))