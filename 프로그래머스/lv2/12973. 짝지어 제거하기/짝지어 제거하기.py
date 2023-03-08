def solution(s):
    stack = [s[0]]
    for i in s[1:]:
        if len(stack) == 0:
            stack.append(i)
            continue

        candidate = stack.pop()
        if  candidate != i:
            stack.append(candidate)
            stack.append(i)

    return 1 if len(stack) == 0 else 0