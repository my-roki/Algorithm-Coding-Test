from itertools import product


def solution(word):
    words_list = []
    for i in range(1, 6):
        words_list += list(map("".join, product("AEIOU", repeat=i)))

    words_list.sort()
    return words_list.index(word) + 1
