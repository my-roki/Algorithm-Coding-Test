def solution(brown, yellow):
    for i in range(1, yellow + 1):
        if yellow % i == 0:
            y_width = max(yellow / i, i)
            y_height = min(yellow / i, i)

            if (y_width + y_height + 2) * 2 == brown:
                b_width = y_width + 2
                b_height = y_height + 2

                return [int(b_width), int(b_height)]
