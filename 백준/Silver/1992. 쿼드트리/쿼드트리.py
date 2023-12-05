import sys


def quad(x: int, y: int, size: int):
    if size == 1:
        return canvas[x][y]

    target = canvas[x][y]
    result = ""
    for i in range(x, x + size):
        for j in range(y, y + size):
            if target != canvas[i][j]:
                size = size // 2
                result += "("
                result += quad(x, y, size)
                result += quad(x, y + size, size)
                result += quad(x + size, y, size)
                result += quad(x + size, y + size, size)
                result += ")"
                return result
    return target


if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())
    canvas = [list(sys.stdin.readline().strip()) for _ in range(N)]
    print(quad(0, 0, N))
