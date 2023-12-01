import sys
from typing import List


def print_canvas(canvas: List[List[int]]):
    for i in canvas:
        print(i)
    print("------------")


def dfs(y: int, x: int) -> None:
    canvas[y][x] = 0
    for dy, dx in direction:
        ny = y + dy
        nx = x + dx
        if ny < 0 or ny >= N or nx < 0 or nx >= M or canvas[ny][nx] == 0:
            continue
        dfs(ny, nx)

    return


if __name__ == "__main__":
    sys.setrecursionlimit(3000)
    direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    T = int(sys.stdin.readline().strip())

    for _ in range(T):
        M, N, K = map(int, sys.stdin.readline().split())
        canvas = [[0] * M for _ in range(N)]
        for _ in range(K):
            X, Y = map(int, sys.stdin.readline().split())
            canvas[Y][X] = 1

        cnt = 0
        for y in range(N):
            for x in range(M):
                if canvas[y][x] == 1:
                    dfs(y, x)
                    cnt += 1

        print(cnt)