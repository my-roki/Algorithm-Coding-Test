def solution(routes: list):
    answer = 0
    stack = []
    routes.sort(key=lambda x:(x[1], x[0]))
    while routes:
        prev = routes.pop(0)
        for _ in range(len(routes)):
            cur = routes.pop(0)
            if prev[1] < cur[0]:  # 둘이 안 곂친다
                stack.append(cur)

        routes = stack
        stack = []
        answer += 1

    return answer