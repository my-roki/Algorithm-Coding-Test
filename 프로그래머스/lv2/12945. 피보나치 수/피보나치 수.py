def solution(n):
    fib = [0,1,1]
    for i in range(3,n+1):
        new_fib = fib[i-1] + fib[i-2]
        fib.append(new_fib)
    return fib[-1] % 1234567