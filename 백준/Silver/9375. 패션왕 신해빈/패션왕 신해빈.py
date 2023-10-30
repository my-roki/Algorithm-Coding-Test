import sys
from collections import defaultdict

if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())

    for _ in range(N):
        M = int(sys.stdin.readline().rstrip())
        cloths_dict = defaultdict(list)
        for _ in range(M):
            # 주어진 옷들을 type별로 분류
            cloth, c_type = sys.stdin.readline().split()
            cloths_dict[c_type].append(cloth)

        # 경우의수 = 각 type + 1 들의 곱 - 1
        # -1 은 아무것도 입지 않은 경우
        result = 1
        for i in cloths_dict.values():
            result *= len(i) + 1

        print(result - 1)
