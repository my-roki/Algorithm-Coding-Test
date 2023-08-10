def solution(rows: int, columns: int, queries: list) -> list:
    answer = []

    # 1. 행렬 만들기
    matrix = [[0] * columns for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            matrix[i][j] = i * columns + j + 1

    # 2. 회전
    for query in queries:
        x1, y1, x2, y2 = query
        # 2-1. 회전할 테두리를 리스트로 만들기
        temp = []
        for i in range(y1 - 1, y2):
            temp.append(matrix[x1 - 1][i])
        for i in range(x1, x2):
            temp.append(matrix[i][y2 - 1])
        for i in range(y2 - 2, y1 - 2, -1):
            temp.append(matrix[x2 - 1][i])
        for i in range(x2 - 2, x1 - 1, -1):
            temp.append(matrix[i][y1 - 1])

        # 2-2. 회전
        temp = [temp[-1]] + temp[:-1]

        # 2-3. 회전한 테두리를 행렬에 적용
        idx = 0
        for i in range(y1 - 1, y2):
            matrix[x1 - 1][i] = temp[idx]
            idx += 1
        for i in range(x1, x2):
            matrix[i][y2 - 1] = temp[idx]
            idx += 1
        for i in range(y2 - 2, y1 - 2, -1):
            matrix[x2 - 1][i] = temp[idx]
            idx += 1
        for i in range(x2 - 2, x1 - 1, -1):
            matrix[i][y1 - 1] = temp[idx]
            idx += 1

        # 3. 최솟값 구하기 - 회전한 테두리에서 가장 작은 값
        answer.append(min(temp))

    return answer