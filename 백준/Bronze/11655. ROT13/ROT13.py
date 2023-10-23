import sys


def rot13(w: str) -> str:
    r = abs(ord(w) + 13)
    if r > ord("z"):
        r = ord("a") + (r - ord("z")) - 1
    return chr(r)


if __name__ == "__main__":
    word = sys.stdin.readline().rstrip()
    result = ""

    for w in word:
        if w.isalpha():
            w_rot13 = rot13(w.lower())

            if w.islower():
                result += w_rot13
            else:
                result += w_rot13.capitalize()
        else:
            result += w
    print(result)