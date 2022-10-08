def solution(arr):
    answer = max(arr)-1
    catch = True
    while catch:
        answer +=1
        for i in arr:
            if answer % i != 0:
                break
        else:
            catch = False

    return answer