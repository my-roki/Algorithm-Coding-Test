from collections import deque


def solution(priorities, location):
    # (location, priority)를 요소로 가지는 queue 생성
    priorities_docs = deque(list(zip(range(len(priorities)), priorities)))

    answer = 0
    while len(priorities_docs) != 0:
        # 현재 남아있는 문서중 우선순위가 가장 높은 번호
        max_priority = max(priorities_docs, key=lambda x: x[1])[1]

        # 현재 queue에서 나온 문서가 최우선 순위 문서인지 확인
        # 만약 최우선 순위가 아니라면 다시 맨 뒤로 넣습니다.
        doc = priorities_docs.popleft()
        if doc[1] < max_priority:
            priorities_docs.append(doc)
            continue

        # 최우선 순위 문서라면 프린트합니다.
        # 프린트 된 문서가 요청한 문서라면 return
        answer += 1
        if doc[0] == location:
            return answer
