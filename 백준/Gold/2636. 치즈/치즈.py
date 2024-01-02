import sys


def print_canvas(canvas):
    for row in canvas:
        print(row)
    print()


def dfs(x, y):
    visited[x][y] = True
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            if canvas[nx][ny] == 0:
                dfs(nx, ny)
            elif canvas[nx][ny] == 1:
                candidate.add((nx, ny))


if __name__ == "__main__":
    """
    1. 0인 특정 가장 자리부터 dfs로 탐색하면서 1인 부분을 찾는다.
    2. 1인 부분을 찾으면 해당 좌표는 겉면이므로 좌표를 저장한다.
    3. 저장된 좌표를 가지고 1인 부분을 0으로 바꾼다(녹아 없어진다).
    4. 1인 부분이 없어질 때까지 반복한다.
    5. 반복이 끝나면 1인 부분이 없어진 횟수와 모두 녹기 직전에 남아있는 치즈조각이 놓여 있는 칸의 개수를 출력한다.
    """
    sys.setrecursionlimit(10004)
    N, M = map(int, sys.stdin.readline().split())
    canvas = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    cnt = 0
    while True:
        visited = [[False] * M for _ in range(N)]
        candidate = set()  # 녹을 치즈의 좌표
        
        # 0인 특정 가장 자리부터 dfs로 탐색하면서 1인 부분을 찾는다.
        dfs(0, 0)

        # 1인 부분이 없어질 때까지 반복한다.
        if not candidate:
            break
        
        # 저장된 좌표를 가지고 1인 부분을 0으로 바꾼다(녹아 없어진다).
        for x, y in candidate:
            canvas[x][y] = 0
        
        cnt += 1  # 1인 부분이 없어진 횟수
        piece = len(candidate)  # 녹기 직전에 남아있는 치즈조각이 놓여 있는 칸의 개수

    print(cnt)
    print(piece)
