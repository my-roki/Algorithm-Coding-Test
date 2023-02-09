def solution(maps: list):
    height = len(maps) - 1
    width = len(maps[0]) - 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    queue = [(0, 0, 0)]
    while len(queue) != 0:
        row, col, move = queue.pop(0)

        # 도착지점에 가장 먼저 도착한 요소의 움직임이 최솟값
        if row == height and col == width:
            return move + 1

        # 상, 하, 좌, 우 이동이 가능한지 확인
        for i in range(4):
            nrow = row + dy[i]
            ncol = col + dx[i]

            # 만약 이동이 가능하다면(맵 초과x, 다음 칸이 이미 지나간 자리가 아님) 이동
            if nrow >= 0 and ncol >= 0 and nrow <= height and ncol <= width and maps[nrow][ncol] > 0:
                maps[nrow][ncol] = 0
                queue.append((nrow, ncol, move + 1))

    return -1
