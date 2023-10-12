import sys

if __name__ == "__main__":
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    arr = [0] * len(alphabet)

    M = sys.stdin.readline().rstrip()

    for m in M:
        idx = alphabet.find(m)
        arr[idx] += 1

    for i in arr:
        print(i, end=" ")
