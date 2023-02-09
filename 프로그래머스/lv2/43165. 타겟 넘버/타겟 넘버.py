"""
0. 스택(stack)를 이용한 dfs -> 구현한 스택 배열 생성.
1. numbers의 가장 첫번째 요소를 더하고 빼는 값을 구합니다.
2. 스택에 새로운 튜플 (numbers에서 연산할 인덱스, 결과)을 담습니다.
3. 모든 numbers를 연산 했다면 결과가 target과 일치하는지 확인합니다.
  3-1. 일치한다면 answer + 1.
  3-2. 일치하지 않는다면 버림.
4. 연산이 아직 끝나지 않았다면 스택에 다시 담아 2번 과정을 계속 반복시킨다.
5. 스택 안에 들어있는 요소들이 전부 없어질때까지 반복한다.
"""


def solution(numbers, target):
    answer = 0
    stack = []  # (인덱스, 결과)를 담는 stack

    stack.append((0, 0))  # 최초 시작
    while len(stack) != 0:
        idx, result = stack.pop()

        if idx < len(numbers):
            plus_result = (idx + 1, result + numbers[idx])
            minus_result = (idx + 1, result - numbers[idx])
            stack.append(plus_result)
            stack.append(minus_result)
        elif result == target:
            answer += 1

    return answer
