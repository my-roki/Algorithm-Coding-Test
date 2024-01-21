import sys
from collections import deque


def input():
    return sys.stdin.readline().strip()


def print_canvas(canvas):
    for c in canvas:
        print(c)
    print()


def bfs(y, x):
    visited = [[0] * N for _ in range(M)]
    q = deque()
    mx = 0

    # init
    q.append((y, x))
    visited[y][x] = 1
    while q:
        y, x = q.popleft()
        for dx, dy in direction:
            nx = x + dx
            ny = y + dy

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if visited[ny][nx] != 0:
                continue
            if canvas[ny][nx] == "W":
                continue

            visited[ny][nx] = visited[y][x] + 1
            q.append((ny, nx))
            mx = max(mx, visited[ny][nx])

    return mx - 1


if __name__ == "__main__":
    M, N = map(int, input().split())
    canvas = [list(input()) for _ in range(M)]
    direction = [(0, 1), (0, -1), (-1, 0), (1, 0)]  # 상하좌우

    result = 0
    for y in range(M):
        for x in range(N):
            if canvas[y][x] == "L":
                mx = bfs(y, x)
                result = max(mx, result)

    print(result)