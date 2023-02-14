def solution(babbling):
    words = ["aya", "ye", "woo", "ma"]
    answer = 0
    for babble in babbling:
        for word in words:
            babble = babble.replace(word, "1")

        babble = babble.replace("1", "")
        if babble == "":
            answer += 1

    return answer