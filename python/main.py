import sys

sys.stdin = open("../input.txt", "r")

import sys

if __name__ == "__main__":
    arr = [0] * 26
    
    M = sys.stdin.readline().rstrip()
    for c in M:
        arr[ord(c) - ord("a")] += 1

    print(" ".join(map(str, arr)))
