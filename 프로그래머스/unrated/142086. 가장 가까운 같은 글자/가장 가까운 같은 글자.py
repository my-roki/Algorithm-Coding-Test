def solution(s):
    answer = []
    alphabet = {}

    for word in s:
        if word not in alphabet:
            answer.append(-1)
        else:
            answer.append(alphabet[word])
        alphabet[word] = 0
        alphabet = {i: alphabet[i] + 1 for i in alphabet}

    return answer