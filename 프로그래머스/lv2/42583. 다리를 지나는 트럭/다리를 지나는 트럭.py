from collections import deque


def solution(bridge_length: int, weight: int, truck_weights: list) -> int:
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    answer = 0

    bridge_weight = 0
    while len(truck_weights) != 0:
        # 다리 통과
        answer += 1
        bridge_weight -= bridge.popleft()

        # 다음 차량이 진입 가능한지 확인합니다.
        truck = truck_weights.popleft()
        if bridge_weight + truck <= weight:
            bridge.append(truck)
            bridge_weight += truck
        else:
            truck_weights.appendleft(truck)
            bridge.append(0)
            bridge_weight += 0

    # 마지막 차량이 들어온 후 bridge의 길이만큼 시간이 흐른 뒤 모든 차량 다리 통과
    return answer + bridge_length
