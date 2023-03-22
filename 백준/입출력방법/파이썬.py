import sys

# 표준입력을 파일로 설정
sys.stdin = open("input.txt", "r")

# Test Case가 여러개의 행으로 이루어졌을경우
"""
3
1 2
3 4 
5 6
"""
TC = int(input().rstrip())

# 공백으로 구분된 2개 숫자 입력 받기
N, M = map(int, sys.stdin.readline().split())

# 하나의 단어 입력받기
N = sys.stdin.readline().rstrip()
