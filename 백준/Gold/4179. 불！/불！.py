import sys
from collections import deque


def input():
    return sys.stdin.readline().strip()


def print_canvas(canvas):
    for c in canvas:
        print(c)
    print()


def has_next(x, y, width, height):
    return x >= 0 and x < width and y >= 0 and y < height


def bfs(queue, visited, who):
    while queue:
        y, x = queue.popleft()
        for dy, dx in direction:
            nx = x + dx
            ny = y + dy

            # 다음 갈 곳이 가장자리면 탈출 가능
            if who == "person" and (x == W - 1 or y == H - 1 or x == 0 or y == 0):
                return visited[y][x]

            if not has_next(nx, ny, W, H):
                continue
            if canvas[ny][nx] == "#" or visited[ny][nx] != init:
                continue
            if who == "person" and fire_visited[ny][nx] <= visited[y][x] + 1:
                continue

            visited[ny][nx] = visited[y][x] + 1
            queue.append((ny, nx))

    return None


if __name__ == "__main__":
    H, W = map(int, input().split())
    canvas = [list(input()) for _ in range(H)]
    direction = [(0, 1), (0, -1), (-1, 0), (1, 0)]  # 상하좌우

    init = sys.maxsize
    fire_visited = [[init] * W for _ in range(H)]
    person_visited = [[init] * W for _ in range(H)]

    person_queue = deque()
    fire_queue = deque()
    for y in range(H):
        for x in range(W):
            if canvas[y][x] == "J":
                person_visited[y][x] = 1
                person_queue.append((y, x))
            if canvas[y][x] == "F":
                fire_visited[y][x] = 1
                fire_queue.append((y, x))

    bfs(fire_queue, fire_visited, who="fire")
    result = bfs(person_queue, person_visited, who="person")

    print(result if result is not None else "IMPOSSIBLE")