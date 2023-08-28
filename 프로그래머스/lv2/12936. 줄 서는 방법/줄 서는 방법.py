def solution(n,k):
    answer = []
    nums = [i for i in range(1,n+1)]
    while n != 0:
        n -= 1
        fact = factorial(n)
        index, k = divmod(k, fact)
        if k == 0:
            answer.append(nums.pop(index-1))
            nums.sort(reverse=True)
            answer += nums
            break
        else:
            answer.append(nums.pop(index))
    return answer

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)


if __name__ == "__main__":
    print(solution(3, 5))  # [3,1,2]