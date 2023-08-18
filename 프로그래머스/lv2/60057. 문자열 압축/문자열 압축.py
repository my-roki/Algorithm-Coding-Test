def solution(s):
    length = len(s)
    min_length = length
    
    for i in range(1, length // 2 + 1):
        count = 1
        temp = s[:i]
        result = ""
        for j in range(i, length, i):
            if temp == s[j:j + i]:
                count += 1
            else:
                result += str(count) + temp if count > 1 else temp
                temp = s[j:j + i]
                count = 1
        result += str(count) + temp if count > 1 else temp
        min_length = min(min_length, len(result))
    return min_length


if __name__ == "__main__":
    print(solution("aabbaccc"))  # 7
    print(solution("ababcdcdababcdcd"))  # 9
    print(solution("abcabcdede"))  # 8
    print(solution("abcabcabcabcdededededede"))  # 14
    print(solution("xababcdcdababcdcd"))  # 17
