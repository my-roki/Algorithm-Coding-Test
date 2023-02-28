from collections import deque


def solution(people: list, limit):
    answer = 0
    people.sort()
    queue = deque(people)
    while queue:
        # queue에 1개의 요소만 남은 경우 1개의 보트를 추가하여 최종 return
        if len(queue) == 1:
            return answer + 1

        max_person = queue.pop()
        min_person = queue.popleft()

        # 보트에 2명만 탑승 가능하니, 가장 무거운 사람과 가벼운 사람의 합이 limit보다 작으면 같이 태우고,
        # 반대인 경우 가장 무거운 사람 혼자만 탈 수 있습니다.
        if max_person + min_person > limit:
            queue.appendleft(min_person)

        answer += 1

    return answer