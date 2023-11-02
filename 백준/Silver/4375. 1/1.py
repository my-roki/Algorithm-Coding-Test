import sys

if __name__ == "__main__":
    while True:
        n = sys.stdin.readline().strip()
        if n == "":
            break
        else:
            n = int(n)

        k = 1
        cnt = 1
        while True:
            if k % n == 0:
                print(cnt)
                break

            k = k * 10 + 1
            k = k % n
            cnt += 1