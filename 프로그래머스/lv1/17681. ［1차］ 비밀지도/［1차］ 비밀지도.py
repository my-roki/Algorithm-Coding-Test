def solution(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1,arr2):
        # 10진수 -> 2진수
        binary_num1 = format(i, 'b')
        binary_num2 = format(j, 'b')
        
        # 2진수 숫자를 더합니다. 맨 앞이 0이라면 자리수만금 앞에 0을 채웁니다.
        binary_result = str(int(binary_num1) + int(binary_num2)).zfill(n)
        
        # 0 : 공백, 1 또는 2 : "#"
        binary_result = binary_result.replace("0", " ")  
        binary_result = binary_result.replace("1", "#")
        binary_result = binary_result.replace("2", "#")
        
        answer.append(binary_result)

    return answer