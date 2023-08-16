from collections import deque


def is_valid(x, y):
    return 0 <= x < 5 and 0 <= y < 5


def bfs(x, y, room):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = set()

    queue = deque([(x, y, 0)])
    visited.add((x, y))

    while queue:
        x, y, dist = queue.popleft()

        if dist > 2:
            continue

        if dist > 0 and room[x][y] == "P":
            return False

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if is_valid(nx, ny) and (nx, ny) not in visited and room[nx][ny] != "X":
                visited.add((nx, ny))
                queue.append((nx, ny, dist + 1))

    return True


def solution(places):
    answer = []
    for room in places:
        is_safe = 1

        for i in range(5):
            for j in range(5):
                if room[i][j] == "P":
                    if not bfs(i, j, room):
                        is_safe = 0
                        break

            if not is_safe:
                break

        answer.append(is_safe)

    return answer