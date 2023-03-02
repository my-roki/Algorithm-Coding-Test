import sys

def solution(n, times):
    answer = sys.maxsize
    left, right = 1, max(times) * n
    while left <= right:
        mid = (left + right) // 2
        done = 0
        for time in times:
            done += mid // time

            if done >= n:
                break

        if done >= n:
            answer = min(answer, mid)
            right = mid - 1
        else:
            left = mid + 1

    return answer
