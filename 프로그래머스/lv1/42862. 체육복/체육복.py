def solution(n, lost, reserve):
    new_lost = set(lost) - set(reserve)
    new_reserve = set(reserve) - set(lost)

    for num in new_reserve:
        front_num = num - 1
        back_num = num + 1
        if front_num in new_lost:
            new_lost.remove(front_num)
        elif back_num in new_lost:
            new_lost.remove(back_num)


    return n - len(new_lost)