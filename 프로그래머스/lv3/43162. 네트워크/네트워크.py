def solution(n: int, computers: list):
    for row in computers:
        print(row)

    computers_clone = computers.copy()
    answer = 0
    for row in range(n):
        for col in range(n):
            if computers_clone[row][col] == 1:
                dfs(row, computers_clone)
                answer += 1

    return answer


def dfs(row, computers):
    for col in range(len(computers[row])):
        if computers[row][col] != 0:
            computers[row][col] = 0
            computers[col][row] = 0
            dfs(col, computers)
