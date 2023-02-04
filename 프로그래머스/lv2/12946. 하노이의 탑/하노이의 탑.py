def hanoi(answer, depth, fromm, to, mid):
    if depth ==1:
        answer.append([fromm,to])
    else:
        hanoi(answer, depth-1, fromm, mid, to)
        answer.append([fromm,to])
        hanoi(answer, depth-1, mid, to, fromm)
        

def solution(n):
    answer = []
    hanoi(answer, n, 1 ,3 , 2)
    return answer