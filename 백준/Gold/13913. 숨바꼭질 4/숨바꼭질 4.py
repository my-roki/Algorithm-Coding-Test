import sys


if __name__ == "__main__":
    n, k = map(int, sys.stdin.readline().split())
    visited = [-1] * 200001
    queue = [(n, 0)]
    path = []

    while queue:
        x, time = queue.pop(0)
        if x == k:
            print(time)
            while x != n:
                path.append(x)
                x = visited[x]
            path.append(n)
            print(" ".join(map(str, path[::-1])))
            break
            
        for nx in [x - 1, x + 1, 2 * x]:
            if 0 <= nx < 200001 and visited[nx] == -1:
                visited[nx] = x
                queue.append((nx, time + 1))
    
    
