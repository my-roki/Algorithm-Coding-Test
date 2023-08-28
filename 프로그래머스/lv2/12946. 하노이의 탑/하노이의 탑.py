def solution(n):
    return hanoi(n, 1, 3, 2)

def hanoi(n, start, end, via):
    if n == 1:
        return [[start, end]]
    else:
        return hanoi(n-1, start, via, end) + [[start, end]] + hanoi(n-1, via, end, start)
    

if __name__ == '__main__':
    print(solution(2))  # [ [1,2], [1,3], [2,3] ]
    print(solution(3))  # [ [1,3], [1,2], [3,2], [1,3], [2,1], [2,3], [1,3] ]
    print(solution(4))  # [[1, 2], [1, 3], [2, 3], [1, 2], [3, 1], [3, 2], [1, 2], [1, 3], [2, 3], [2, 1], [3, 1], [2, 3], [1, 2], [1, 3], [2, 3]]