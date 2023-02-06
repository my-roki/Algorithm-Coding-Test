"""
1. 각 던전을 돌 수 있는 경우의 수를 모두 구합니다.
2. 각 경우에수에 대하여 시뮬레이션을 돌립니다.
3. 시뮬레이션 결과중 최댓값을 리턴합니다.
"""

from itertools import permutations


def solution(k, dungeons):
    answer = -1
    candidate = permutations(dungeons, len(dungeons))
    for c_dugeons in candidate:
        cnt = 0  # 탐험 횟수 초기화
        new_k = k  # 스테미나 초기화
        for dugeon in c_dugeons:
            if new_k >= dugeon[0]:
                new_k -= dugeon[1]
                cnt += 1
            else:
                break

        if answer <= cnt:
            answer = cnt

    return answer
