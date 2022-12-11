def solution(s):
    answer = []
    check = {}

    for word in s:
        if word not in check:
            answer.append(-1)
        else:
            answer.append(check[word])
        check[word] = 0
        check = {i: check[i] + 1 for i in check}

    return answer