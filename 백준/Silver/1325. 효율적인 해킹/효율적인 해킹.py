import sys
from typing import List
from collections import deque


def dfs(here: int, nodes: List[List[int]], visited: List[bool]):
    result = 1
    visited[here] = True
    for neighbor in nodes[here]:
        if not visited[neighbor]:
            result += dfs(neighbor, nodes, visited)
    return result


def bfs(start: int, nodes: List[List[int]], visited: List[bool]) -> int:
    queue = deque([start])
    visited[start] = True
    count = 1

    while queue:
        current = queue.popleft()
        for neighbor in nodes[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                count += 1
    return count


if __name__ == "__main__":
    sys.setrecursionlimit(10004)

    N, M = map(int, sys.stdin.readline().split())
    nodes = [[] for _ in range(N + 1)]
    for _ in range(M):
        A, B = map(int, sys.stdin.readline().split())
        nodes[B].append(A)

    visited = [False] * (N + 1)
    max_count = 0
    max_nodes = []
    for n in range(1, N + 1):
        visited = [False] * (N + 1)  # Reset visited for each node
        count = bfs(n, nodes, visited)
        if count > max_count:
            max_count = count
            max_nodes = [n]
        elif count == max_count:
            max_nodes.append(n)

    print(" ".join(map(str, max_nodes)))
