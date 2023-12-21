import sys

if __name__ == "__main__":
    T = int(sys.stdin.readline().strip())
    for _ in range(T):
        arr = list(sys.stdin.readline().strip())
        stack = []
        for cur in arr:
            if len(stack) == 0:
                stack.append(cur)
                continue

            last = stack.pop()
            if cur == ")" and last == "(":
                continue
            else:
                stack.append(last)
                stack.append(cur)
        
        result = "YES" if len(stack) == 0 else "NO"
        print(result)