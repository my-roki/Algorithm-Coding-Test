from collections import defaultdict


def solution(tickets):
    answer = []
    tickets.sort(key=lambda x: x[1], reverse=True)

    travels = defaultdict(list)
    for src, dst in tickets:
        travels[src].append(dst)

    src = "ICN"
    current_list = []
    current_list.append(src)
    while current_list:
        current = current_list[-1]
        next_list = travels.get(current)

        # 다음 갈 곳이 없는 경우가 현재 위치에서 최종 위치가 됩니다.
        if next_list == None or len(next_list) == 0:
            answer.append(current_list.pop())
        # 다음 갈 곳이 있는 경우 그 다음 경로에서 최종경로를 재탐색합니다.
        else:
            current_list.append(travels[current].pop())
    # 최종 - 전최종 - 전전최종 ... - 출발 이런식으로 append 했기 때문에 reverse
    answer.reverse()
    return answer
