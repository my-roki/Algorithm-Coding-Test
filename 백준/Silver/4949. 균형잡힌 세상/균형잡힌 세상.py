import sys

if __name__ == "__main__":
    T = None
    while T != ".":
        T = sys.stdin.readline().rstrip()
        if T == ".":
            break

        stack = []
        bracket = ["(", ")", "[", "]"]
        for cur in T:
            if cur not in bracket:
                continue

            if len(stack) == 0:
                stack.append(cur)
                continue

            last = stack.pop()
            if cur == ")" and last == "(":
                continue
            elif cur == "]" and last == "[":
                continue
            else:
                stack.append(last)
                stack.append(cur)

        result = "yes" if len(stack) == 0 else "no"
        print(result)
