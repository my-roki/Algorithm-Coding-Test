import sys

N = sys.stdin.readline()
W, H = map(int, sys.stdin.readline().split())

# 주어진 점의 좌표를 배열에 담는다.
points = set()
for _ in range(int(N)):
    X, Y = map(int, sys.stdin.readline().split())
    points.add((X, Y))

# 점의 좌표를 기준으로 사각형을 만들 수 있는지 확인한다.
cnt = 0
for p in points:
    w, h = p
    p1 = (w, h + H)
    p2 = (w + W, h)
    p3 = (w + W, h + H)

    # 점의 좌표가 모두 배열(포인트로 만들 수 있는지)에 있는지 확인한다.
    if p1 in points and p2 in points and p3 in points:
        cnt += 1

print(cnt)
