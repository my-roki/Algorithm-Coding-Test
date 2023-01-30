def solution(n):
    ternary_num_reverse = ""
    while n != 0:
        quo = n // 3
        div = n % 3
        ternary_num_reverse += str(div)
        n = quo

    answer = 0
    for idx, i in enumerate(ternary_num_reverse[::-1]):
        answer += int(i) * (3**idx)

    return answer
