def solution(numbers):
    str_numbers = [str(i) for i in numbers]
    
    # lambda x: x*3 이유는 자릿수가 4개 이하이니까 문자열을 3번 이상 반복해서 비교를 해야함
    str_numbers.sort(key=lambda x: x*3, reverse=True)
    
    # [0, 0, 0, 0] test case -> "0000" (x) / "0" (o)
    answer = str(int(''.join(str_numbers)))
    return answer

