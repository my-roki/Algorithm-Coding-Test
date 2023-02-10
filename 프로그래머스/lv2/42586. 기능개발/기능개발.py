"""
1. 현재 progress에서 100까지 되려면 필요한 날을 구합니다. 
2. 현재 작업이 이전 작업들보다 늦게 완료가 되면 현재 작업 전 작업까지만 배포가 됩니다.
3. 현재 작업이 이전 작업보다 빨리 완료가 된다면 이전 작업들과 함께 배포가 됩니다.
"""


import math


def solution(progresses, speeds):
    # 작업이 완료되기까지 남은 일수를 구합니다.
    remains = [math.ceil((100 - progress) / speed) for progress, speed in zip(progresses, speeds)]

    answer = []
    deploy = 0
    biggest = remains[0]  # 기준값
    for idx in range(1, len(remains)):
        # 현재 작업이 이전 작업들에 비해 더 오래걸리면 이 작업은 다음에 배포되어야 합니다.
        if remains[idx] > biggest:
            # 현재 작업 포함, 이전 배포할 수 있는 작업들의 개수을 answer에 담고 배포 카운트 초기화
            answer.append(deploy + 1)
            deploy = 0
            biggest = remains[idx]
        # 현재 작업이 이전 작업들에 비해 빨리 끝났다면(작업일이 적어 다 돼고 기다리고 있는것) 같이 배포될 수 있습니다.
        else:
            deploy += 1  # 적립
    else:
        answer.append(deploy + 1)  # 마지막은 무조건 마지막 날에 배포가 됩니다.

    return answer