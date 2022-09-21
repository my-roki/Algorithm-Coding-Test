def hanoi(start, end, n):
    if n == 1:
        print(f"{start} {end}")
    else:
        rest = 6 - start - end
        hanoi(start, rest, n - 1)
        print(f"{start} {end}")
        hanoi(rest, end, n - 1)


if __name__ == "__main__":
    N = int(input())
    print(2**N - 1)
    if N <= 20:
        hanoi(1, 3, N)
