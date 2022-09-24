import math

def compress(n,string):
    result = ""
    count = 1
    for i in range(0, len(string), n):
        if string[i : i + n] == string[i + n : i + (2 * n)]:
            count += 1
        else:
            if count == 1:
                result += string[ i : i + n] 
            else:
                result += f"{count}{string[i : i + n]}"
                count = 1
    return result
            


def solution(s):
    answer = len(s)
    for i in range(1, math.floor(len(s)/2)+1):
        result = len(compress(i, s))
        if result < answer:
            answer = result
    return answer