import sys


if __name__ == "__main__":
    H, W = map(int, sys.stdin.readline().split())
    result = [[-1] * W for _ in range(H)]

    for r in result:
        I = sys.stdin.readline().strip()
        cnt = 0
        initial = True
        for idx, i in enumerate(I):
            if i == "c" and initial:
                initial = False
                r[idx] = cnt
                continue

            if i == "c" and not initial:
                cnt = 0
                r[idx] = cnt
                continue

            if i == "." and not initial:
                cnt += 1
                r[idx] = cnt
                continue

            if i == "." and initial:
                continue
        print(" ".join(map(str, r)))