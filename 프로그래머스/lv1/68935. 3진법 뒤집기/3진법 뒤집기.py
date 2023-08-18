def solution(n: int) -> int:
    return convert3to10(convert10to3(n)[::-1])


# 10진법 -> 3진법 변환
def convert10to3(n: int) -> str:
    T = "0123456789"
    q, r = divmod(n, 3)
    return T[r] if q == 0 else convert10to3(q) + T[r]


# 3진법 -> 10진법 변환
def convert3to10(n: str) -> int:
    answer = 0
    for idx, num in enumerate(n[::-1]):
        answer += int(num) * (3**idx)
    return answer


if __name__ == "__main__":
    print(solution(45))  # 7
    print(solution(125))  # 229
