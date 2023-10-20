import sys
from collections import defaultdict


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())

    fn_dict = defaultdict(int)
    for _ in range(N):
        fn = sys.stdin.readline().rstrip()[0]
        fn_dict[fn] += 1

    result = ""
    for key, value in fn_dict.items():
        if value >= 5:
            result += key

    print("".join(sorted(result)) if result != "" else "PREDAJA")