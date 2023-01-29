import sys

N = int(input())

for _ in range(N):
    testcase = sys.stdin.readline().rstrip()
    answer = ["".join(list(i)[::-1]) for i in testcase.split(" ")]
    print(" ".join(answer))
