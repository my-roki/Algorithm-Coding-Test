def solution(s):
    cnt = num = 0
    while s != '1':
        cnt += s.count('0')
        s = bin(s.count('1'))[2:]
        num += 1

    return [num, cnt]