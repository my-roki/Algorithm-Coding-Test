import sys


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())

    num = "0123456789"
    arr = []
    for _ in range(N):
        word = sys.stdin.readline().strip()
        candidate = ""
        for w in word:
            if w not in num and candidate != "":
                arr.append(candidate)
                candidate = ""
            elif w not in num and candidate == "":
                continue
            else:
                candidate += w
        else:
            arr.append(candidate) if candidate != "" else None

    arr = list(map(int, arr))
    arr.sort()
    for i in arr:
        print(i)