import sys

"""
100 x 100의 0으로 채운 배열을 만듭니다.
각 색종이 정보를 통해 채워진 영역에는 1로 채웁니다.
(중복된 영역은 배열 안의 값과 관계없이 1로 새롭게 할당 되므로 곂쳐지는 문제를 쉽게 해결 가능합니다.)
모든 색종이를 채웠으면 배열에서 1인 요소들의 합을 구합니다.(1 x 1의 면적은 1)
"""

N = int(input())

arr = [[0] * 101 for i in range(101)]  # 101개를 만드는 이유는 배열의 인덱스가 0부터 시작해서 사용자 편의를 위해 첫 행령(0)은 무시하도록 설정
for _ in range(N):
    X, Y = map(int, sys.stdin.readline().split())

    for i in range(10):
        for j in range(10):
            arr[Y + i][X + j] = 1

answer = sum([sum(i) for i in arr])
print(answer)
