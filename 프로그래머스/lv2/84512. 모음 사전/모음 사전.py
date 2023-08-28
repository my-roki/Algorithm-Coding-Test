def solution(word):
    dictionary = []
    make_dictionary(dictionary, 0, "")
    return dictionary.index(word) + 1


def make_dictionary(dictionary, length, word):
    if length > 5:
        return dictionary
    if word != "":
        dictionary.append(word)
    for i in ["A", "E", "I", "O", "U"]:
        make_dictionary(dictionary, length + 1, word + i)


if __name__ == "__main__":
    print(solution("AAAAE"))  # 6
    print(solution("AAAE"))  # 10
    print(solution("I"))  # 1563
    print(solution("EIO"))  # 1189
