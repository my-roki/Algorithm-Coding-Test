import math
from itertools import permutations


def solution(numbers):
    answer = set()
    for i in range(1, len(numbers) + 1):
        for p in permutations(list(numbers), i):
            if is_prime(int("".join(p))):
                answer.add(int("".join(p)))

    return len(answer)


def is_prime(number):
    if number == 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            return False
    else:
        return True