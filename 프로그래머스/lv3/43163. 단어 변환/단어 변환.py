from collections import deque


def solution(begin, target, words):
    # 무조건 변환이 될 수 없는 경우
    if target not in words:
        return 0

    queue = deque()
    queue.append([begin, []])

    while queue:
        begin, changes = queue.popleft()
        for word in words:
            if word not in changes and is_change(word, begin):
                if word == target:
                    return len(changes) + 1
                new_changes = changes.copy()
                new_changes.append(word)
                queue.append([word, new_changes])
    return 0


def is_change(src, dst):
    cnt = 0
    for i in range(len(dst)):
        if src[i] != dst[i]:
            cnt += 1

    return True if cnt == 1 else False
