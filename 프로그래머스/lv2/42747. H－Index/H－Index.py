def solution(citations):
    citations.sort()

    for idx, h in enumerate(citations):
        if h >= len(citations) - idx:
             return len(citations) - idx
    return 0
