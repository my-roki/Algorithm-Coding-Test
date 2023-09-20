from typing import List


def solution(n: int, times: List[int]) -> int:
    # 이진 탐색

    # 1. left = 1, right = 심사시간 최댓값 * n
    # 1-1. 심사시간 최댓값은 가장 오래 걸리는 심사관이 모든 사람을 심사할 때이다.
    # 1-2. 심사시간의 모든 경우의 수를 가지고 가장 적게 걸리는 시간을 탐색.

    # 2. 중간값을 기준으로 특정 시간동안 심사할 수 있는 사람의 수를 구한다.
    # 2-1. 중간값에서 각 심사위원이 심사할 수 있는 사람의 수를 구한다.
    # 2-2. 중간값에서 각 심사위원이 심사할 수 있는 사람의 수 의 합(sum_people)에 따라 left, right를 조정한다.
    # 2-3. sum_people < n 이면 left = mid + 1, sum_people >= n 이면 right = mid

    # 3. left == right가 될 때까지 반복한다. => left가 최소 시간이 된다.

    left = 1
    right = max(times) * n

    while left != right:
        mid = (left + right) // 2
        sum_people = 0
        for time in times:
            sum_people += mid // time
            if sum_people >= n:
                break

        if sum_people >= n:
            right = mid
        else:
            left = mid + 1

    return left


if __name__ == "__main__":
    n = 6
    times = [7, 10]
    print(solution(n, times))  # 28
