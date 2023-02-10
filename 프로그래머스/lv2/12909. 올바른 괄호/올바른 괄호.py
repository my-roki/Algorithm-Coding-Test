def solution(s):
    stack = []
    for i in s:
        # 스택 안에 아무것도 없다면 비교할 것이 없으므로 바로 스택에 문자를 담습니다.
        if len(stack) == 0:
            stack.append(i)
            continue

        # 스택의 마지막 요소가 "(", 현재 비교하려는 문자가 ")"이면 짝짓기 성공.
        if stack[-1] + i == "()":
            stack.pop()
        else:
            stack.append(i)

    # 올바른 괄호는 결국 스택에 남은 요소가 없어야합니다.( "(", ")"으로 짝짓기 돼서 없음)
    return True if len(stack) == 0 else False
