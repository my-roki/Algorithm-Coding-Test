def solution(array, commands):
    answer = []
    for command in commands:
        i = command[0]
        j = command[1]
        k = command[2]
        slice_array = array[i - 1 : j]
        slice_array.sort()
        num = slice_array[k - 1]
        
        answer.append(num)
    return answer