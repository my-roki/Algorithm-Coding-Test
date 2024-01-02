import sys
from itertools import combinations


def print_canvas(canvas):
    for row in canvas:
        print(row)
    print()


if __name__ == "__main__":
    """
    1. 벽을 세울 수 있는 모든 경우의 수를 수한다.
    2. 각 경우의 수에서 벽을 세울 경우 퍼지는 바이러스를 구한다.
    3. 각 경우의 수에서 안전 영역을 구한다.
    4. 안전 영역의 최대값을 구한다.
    """

    N, M = map(int, sys.stdin.readline().split())
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    # 1. 벽을 세울 수 있는 모든 경우의 수를 수한다.
    empty_space = []
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                empty_space.append((i, j))

    wall_candidates = list(combinations(empty_space, 3))

    # 2. 각 경우의 수에서 벽을 세울 경우 퍼지는 바이러스를 구한다.
    max_safe_area = 0
    for wall_candidate in wall_candidates:
        board_copy = [row[:] for row in board]
        for i, j in wall_candidate:
            board_copy[i][j] = 1

        # 3. 각 경우의 수에서 안전 영역을 구한다.
        visited = [[False] * M for _ in range(N)]
        for i in range(N):
            for j in range(M):
                if board_copy[i][j] == 2:
                    stack = [(i, j)]
                    visited[i][j] = True
                    while stack:
                        x, y = stack.pop()
                        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < N and 0 <= ny < M and board_copy[nx][ny] == 0 and not visited[nx][ny]:
                                stack.append((nx, ny))
                                visited[nx][ny] = True
                                board_copy[nx][ny] = 2

        # 4. 안전 영역의 최대값을 구한다.
        safe_area = sum([row.count(0) for row in board_copy])
        max_safe_area = max(max_safe_area, safe_area)

    print(max_safe_area)