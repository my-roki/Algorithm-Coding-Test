def solution(food):
    answer = ""
    for idx in range(1, len(food)):
        answer += str(idx) * divmod(food[idx], 2)[0]

    return answer + "0" + answer[::-1]
