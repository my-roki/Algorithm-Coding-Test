from itertools import combinations


def solution(line: list):
    # line array 에서 2개를 뽑아 만들 수 있는 모든 경우의 수를 구하는 코드 구현
    comb = list(combinations(line, 2))

    # 2. 1번에서 구한 경우의 수를 이용해 정수 교점이 존재하는지 확인
    arr = [get_intersection(i[0], i[1]) for i in comb if get_intersection(i[0], i[1])]
    print(arr)

    # 3. 좌표를 이용해 그림을 그림
    max_x = max(arr, key=lambda x: x[0])[0]
    max_y = max(arr, key=lambda x: x[1])[1]

    min_x = min(arr, key=lambda x: x[0])[0]
    min_y = min(arr, key=lambda x: x[1])[1]


    answer = ["." * (max_x - min_x + 1) for _ in range(max_y - min_y + 1)]
    for i in arr:
        answer[i[1] - min_y] = answer[i[1] - min_y][: i[0] - min_x] + "*" + answer[i[1] - min_y][i[0] - min_x + 1 :]
    
    answer.reverse()
    return answer


def get_intersection(line1: list, line2: list):
    a = line1[0]
    b = line1[1]
    e = line1[2]

    c = line2[0]
    d = line2[1]
    f = line2[2]

    if a * d - b * c == 0:
        return None

    x = (b * f - e * d) / (a * d - b * c)
    y = (e * c - a * f) / (a * d - b * c)

    if x.is_integer() and y.is_integer():
        return [int(x), int(y)]
