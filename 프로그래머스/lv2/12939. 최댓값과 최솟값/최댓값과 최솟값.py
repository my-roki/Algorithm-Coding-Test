def solution(s):
    s_list = list(map(int,s.split(" ")))
    s_min = min(s_list)
    s_max = max(s_list)
    answer = f"{s_min} {s_max}"
    return answer