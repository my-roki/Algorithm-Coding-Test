"""
1. 노란색으로 만들 수 있는 사각형의 경우의 수를 구합니다.
2. 1번의 경우의 수에서 테두리 1줄을 주어진 갈색으로 채울 수 있는지 확인해야 합니다.
3. 노란색 종이의 (가로 + 세로 + 2) * 2 = 갈색 종이 개수인 경우의 수를 찾습니다.
4. [노란색 가로 + 2, 노란색 세로 + 2]을 리턴합니다.
"""


import math


def solution(brown, yellow):
    # 가로 * 세로를 만들 수 있는 것은 yellow의 약수입니다.
    for i in range(1, int(yellow ** (1 / 2)) + 1):
        if yellow % i != 0:
            continue
            
        # 카펫의 가로 길이는 세로 길이와 같거나, 세로 길이보다 깁니다.
        y_width = max(yellow / i, i)  
        y_height = min(yellow / i, i)

        if (y_width + y_height + 2) * 2 != brown:
            continue

        return [int(y_width + 2), int(y_height + 2)]

    # 혹시 안 되는 경우가 있나?!
    else:
        print("가능한 조합이 없습니다!")
        return None
