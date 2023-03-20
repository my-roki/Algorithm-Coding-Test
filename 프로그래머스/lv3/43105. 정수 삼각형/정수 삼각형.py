"""
동적 계획법
1. 각 삼각형 층에서 윗층의 숫자를 더할 수 있는경우 중 최댓값들을 누적해서 맨 아래층까지 갑니다.
1-1. 현재 층의 가장 왼쪽에 있는 숫자는 윗층의 가장 왼쪽의 숫자를 더합니다.
1-2. 현재 층의 가장 오른쪽에 있는 숫자는 윗층의 가장 오른쪽의 숫자를 더합니다.
1-3. 현재 층의 중간 숫자는 윗층의 오른쪽 숫자 또는 왼쪽숫자 중 더 큰 수를 더합니다.

    7              7                 7                   7                  7           
   3 8           10 15            10   15             10   15            10   15         
  8 1 0         8  1  0          18  16  15          18  16  15         18  16  15        
 2 7 4 4       2  7  4  4       2   7   4   4       20  25  20  19     20  25  20  19      
4 5 2 6 5     4  5  2  6  5    4  5   2   6   5    4  5   2   6   5   24 30  27  26  14    

2. 가장 아랫층까지 연산이 끝나면 가장 아랫층의 숫자 중 최대값을 리턴합니다.
"""


def solution(triangle):
    for row_idx in range(1, len(triangle)):
        for col_idx in range(row_idx + 1):
            if col_idx == 0:  # 가장 왼쪽의 숫자인 경우
                triangle[row_idx][col_idx] += triangle[row_idx - 1][col_idx]
            elif col_idx == row_idx:  # 가장 오른쪽의 숫자인 경우
                triangle[row_idx][col_idx] += triangle[row_idx - 1][col_idx - 1]
            else:  # 중간의 숫자인 경우
                triangle[row_idx][col_idx] += max(triangle[row_idx - 1][col_idx], triangle[row_idx - 1][col_idx - 1])

    return max(triangle[len(triangle) - 1])
