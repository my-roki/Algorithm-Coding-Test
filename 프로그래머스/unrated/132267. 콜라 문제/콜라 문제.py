def solution(a, b, n):
    answer = 0
    while n >= a:
        new_coke = (n // a) * b
        rest_coke = n % a
        n = new_coke + rest_coke

        answer += new_coke

    return answer