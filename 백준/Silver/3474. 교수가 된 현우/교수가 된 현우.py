import sys

if __name__ == "__main__":
    T = int(sys.stdin.readline())

    for _ in range(T):
        # 5의 인수 개수만큼 0이 붙음 (5, 10, 15, 20, 25(5 * 5), ..., 50(5 * 5 * 2), 55, 60 => 14개)
        N = int(sys.stdin.readline())
        result = 0
        cur5 = 5
        while True:
            q = N // cur5
            if q == 0:
                break
            result += q
            cur5 *= 5

        print(result)