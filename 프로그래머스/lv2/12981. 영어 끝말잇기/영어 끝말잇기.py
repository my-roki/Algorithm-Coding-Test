def solution(n, words):
    word = [words[0]]
    for i in range(1, len(words)):
        # 이전에 등장했던 단어 확인
        if words[i] in word:
            return [i % n + 1, i // n + 1]

        # 앞사람이 말한 단어의 마지막 문자로 시작하는 단어 확인
        if words[i][0] == word[-1][-1]:
            word.append(words[i])
        else:
            return [i % n + 1, i // n + 1]

    return [0, 0]
