def solution(answers):
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    one_cnt = two_cnt = three_cnt = 0

    for idx, i in enumerate(answers):
        if i == one[idx % len(one)]:
            one_cnt += 1
        if i == two[idx % len(two)]:
            two_cnt += 1
        if i == three[idx % len(three)]:
            three_cnt += 1

    result = [one_cnt, two_cnt, three_cnt]
    answer = [j + 1 for j in range(len(result)) if result[j] == max(result)]

    return answer
