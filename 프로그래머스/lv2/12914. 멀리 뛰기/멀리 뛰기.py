def solution(n):
    a, b = 1, 1
    if n == 1:
        return 1
    for i in range(2, n + 1):
        a, b = a + b, a

    return a % 1234567
