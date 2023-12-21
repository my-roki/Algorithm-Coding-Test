import sys

if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    init = 666
    while N != 1:
        init += 1
        if "666" in str(init):
            N -= 1
    
    print(init)
