import sys
from typing import List
from collections import deque


def print_canvas(canvas: List[List[int]]):
    for i in canvas:
        print(i)
    print("------------")


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().rstrip().split())
    canvas = [list(map(int, list(i.rstrip()))) for i in sys.stdin.readlines()]
    c_width, c_height = len(canvas[0]), len(canvas)
    visited = [[0] * len(canvas[0]) for _ in range(len(canvas))]
    direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    q = deque()
    q.append((0, 0))
    visited[0][0] = 1
    while len(q):
        y, x = q.popleft()

        for dy, dx in direction:
            ny = y + dy
            nx = x + dx

            if ny < 0 or ny >= c_height or nx < 0 or nx >= c_width or canvas[ny][nx] == 0:
                continue
            if visited[ny][nx] != 0:
                continue

            visited[ny][nx] = visited[y][x] + 1

            q.append((ny, nx))

    # print_canvas(canvas)
    # print_canvas(visited)
    print(visited[N - 1][M - 1])