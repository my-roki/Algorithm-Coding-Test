def solution(arr1, arr2):
    answer = []
    
    for i in range(len(arr1)): # arr1의 row 수
        temp = []
        arr = arr1[i]
        for j in range(len(arr2[0])): # arr2의 columns 수
            num = 0
            for k in range(len(arr2)): # arr2의 row 수
                num += arr[k] * arr2[k][j]
            temp.append(num)
        answer.append(temp)
    
    return answer