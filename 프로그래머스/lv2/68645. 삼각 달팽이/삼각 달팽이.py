def solution(n: int):
    # 1-1. 달팽이가 움직일 수 있는 삼각형
    triangle = [[0] * i for i in range(1, n + 1)]
    max_int = sum(i for i in range(1, n + 1))

    # 1-2. 달팽이가 움직이는 방향은 아래, 오른쪽, 11시 대각선 순서로 이루어지므로 3의 나머지를 이용한다.
    d = 0  # 0: 아래, 1: 오른쪽, 2: 대각선
    d_row = [1, 0, -1]  # direction에 따른 y축 이동 방향
    d_col = [0, 1, -1]  # direction에 따른 x축 이동 방향
    row, col = 0, 0  # 현재 달팽이의 위치

    # 2. 삼각형이 다 채워질때까지 숫자를 채워가며 움직인다.
    cnt = 1
    while cnt <= max_int:
        triangle[row][col] = cnt

        # 2-1. 다음 좌표를 달팽이가 갈 수 있는지 검사한다.
        n_row = row + d_row[d]
        n_col = col + d_col[d]

        # 2-2. 다음 좌표가 삼각형 내에 있는 좌표 and 다음 좌표에 한번도 방문하지 않았으면 이동.
        if (n_row >= 0 and n_row < n and n_col >= 0 and n_col < n) and (triangle[n_row][n_col]) == 0:
            row = n_row
            col = n_col
        # 갈 수 있는 방향으로 끝까지 갔거나, 이미 방문한 좌표라면 방향을 바꿔서 이동한다.
        else:
            d = (d + 1) % 3
            row += d_row[d]
            col += d_col[d]

        cnt += 1

    # 이중 리스트를 flatten 하는 방법
    # https://docs.python.org/ko/3/library/functions.html#sum
    return sum(triangle, [])