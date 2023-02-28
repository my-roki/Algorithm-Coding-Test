def solution(name: str):
    answer = 0
    move = len(name) - 1
    for idx, i in enumerate(name):
        answer += min(ord(i) - ord("A"), ord("Z") - ord(i) + 1)

        next_idx = idx + 1
        while next_idx < len(name) and name[next_idx] == "A":
            next_idx += 1

        # 정방향으로 이동하는 경우 vs
        # 정방향으로 갔다가 연속된 A를 만나 역방향으로 이동하는 경우 vs
        # 역방향으로 갔다가 연속된 A를 만나 정방향으로 이동하는 경우
        move = min(
            [
                move,
                2 * idx + len(name) - next_idx,
                idx + 2 * (len(name) - next_idx),
            ]
        )

    return answer + move