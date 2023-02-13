def solution(prices):
    answer = []
    for i in range(len(prices)):
        time = 0
        for j in range(i + 1, len(prices)):
            time += 1
            if prices[i] > prices[j]:  # 가격이 떨어졌으면 거기까지 시간을 측정
                break
        answer.append(time)
    return answer
