import sys


if __name__ == "__main__":
    while True:
        word = sys.stdin.readline().rstrip()
        if word == "end":
            break

        # 1. 모음(a,e,i,o,u) 하나를 반드시 포함하여야 한다.
        cond_1 = [word.count(c) > 0 for c in "aeiou"]
        if not any(cond_1):
            print(f"<{word}> is not acceptable.")
            continue

        # 2. 모음이 3개 혹은 자음이 3개 연속으로 오면 안 된다.
        flag = False
        for i in range(len(word) - 2):
            # 모음이 3개 연속으로 오면 안 된다.
            if word[i] in "aeiou" and word[i + 1] in "aeiou" and word[i + 2] in "aeiou":
                flag = True
                break
            # 자음이 3개 연속으로 오면 안 된다.
            elif word[i] not in "aeiou" and word[i + 1] not in "aeiou" and word[i + 2] not in "aeiou":
                flag = True
                break
        if flag:
            print(f"<{word}> is not acceptable.")
            continue

        # 3. 같은 글자가 연속적으로 두번 오면 안되나, ee 와 oo는 허용한다.
        cond_3 = [word[i] == word[i + 1] and word[i] not in "eo" for i in range(len(word) - 1)]
        if any(cond_3):
            print(f"<{word}> is not acceptable.")
            continue

        print(f"<{word}> is acceptable.")