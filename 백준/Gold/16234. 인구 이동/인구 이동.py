import sys
from collections import deque


def input():
    return sys.stdin.readline().strip()


def print_canvas(canvas):
    for c in canvas:
        print(c)
    print()


def bfs(y, x):
    q = deque()
    q.append((y, x))
    xy_index = []
    xy_index.append((y, x))
    visited[y][x] = True
    populations = canvas[y][x]
    while q:
        y, x = q.popleft()
        for dy, dx in direction:
            nx = x + dx
            ny = y + dy
            if ny < 0 or ny >= N or nx < 0 or nx >= N:
                continue
            if visited[ny][nx]:
                continue
            if L <= abs(canvas[ny][nx] - canvas[y][x]) <= R:
                visited[ny][nx] = True
                q.append((ny, nx))
                xy_index.append((ny, nx))
                populations += canvas[ny][nx]
    for y, x in xy_index:
        canvas[y][x] = populations // len(xy_index)
    return len(xy_index)


if __name__ == "__main__":
    N, L, R = map(int, input().split())
    canvas = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    direction = [(0, 1), (0, -1), (-1, 0), (1, 0)]  # 상하좌우

    cnt = 0
    while True:
        visited = [[False] * N for _ in range(N)]
        flag = False
        for y in range(N):
            for x in range(N):
                if not visited[y][x]:
                    if bfs(y, x) > 1:
                        flag = True
        if not flag:
            break
        cnt += 1

    print(cnt)