def solution(clothes):
    dict = {}
    for _, key in clothes:
        if key not in dict:
            dict[key] = 2
        else:
            dict[key] += 1
    
    answer = 1
    for value in dict.values():
        answer *= value
    
    return answer - 1