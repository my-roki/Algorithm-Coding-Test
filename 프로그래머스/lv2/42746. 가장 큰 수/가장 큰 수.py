def solution(numbers):
    str_numbers = [str(i) for i in numbers]
    str_numbers.sort(key=lambda x: x*3, reverse=True)
    
    # [0, 0, 0, 0] test case -> "0000" (x) / "0" (o)
    answer = str(int(''.join(str_numbers)))
    return answer

