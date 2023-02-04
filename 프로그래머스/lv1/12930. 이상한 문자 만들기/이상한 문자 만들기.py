def solution(s):
    words = s.split(" ")
    new_list = []
    for word in words:
        new_word = ""
        for idx, char in enumerate(word):
            if idx % 2 == 0:
                new_word += char.upper()
            else:
                new_word += char.lower()
        new_list.append(new_word)
    answer = " ".join(new_list)
    return answer
