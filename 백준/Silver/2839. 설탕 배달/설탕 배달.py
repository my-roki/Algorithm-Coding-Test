import sys


def solution(N: int) -> int:
    kg5, mod = divmod(N, 5)

    kg3 = 0
    while mod != 0 and kg5 >= 0:
        kg3, mod = divmod(mod, 3)
        if mod != 0:
            kg5 -= 1
            mod += (kg3 * 3) + 5

    return kg5 + kg3 if kg5 + kg3 != 0 and kg5 >= 0 and kg3 >= 0 else -1


for N in sys.stdin.readlines():
    print(solution(int(N)))
