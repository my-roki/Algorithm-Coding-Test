from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):
    characterX *= 2
    characterY *= 2
    itemX *= 2
    itemY *= 2
    canvas = [[-1] * 102 for _ in range(102)]

    # 1칸 근접해있을 때 경로 문제가 발생하여 사이즈를 2배 늘려 근접한 경로 문제 해결
    for r in rectangle:
        xbl, ybl, xtr, ytr = map(lambda x: x * 2, r)
        for x in range(xbl, xtr + 1):
            for y in range(ybl, ytr + 1):
                if xbl < x < xtr and ybl < y < ytr:
                    canvas[y][x] = 0
                elif canvas[y][x] != 0:
                    canvas[y][x] = 1

    # bfs
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    visited = [[1] * 102 for i in range(102)]
    queue.append([characterX, characterY])

    while queue:
        x, y = queue.popleft()

        # 현재 좌표가 도착점이라면 return
        if x == itemX and y == itemY:
            return visited[y][x] // 2

        # 각 방향마다 이동할 수 있는 좌표인지 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if canvas[ny][nx] == 1 and visited[ny][nx] == 1:
                queue.append([nx, ny])
                visited[ny][nx] = visited[y][x] + 1

    return -1