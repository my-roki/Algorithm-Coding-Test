import sys


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().strip().split())

    poketmons_number = {}
    poketmons_name = {}

    for i in range(N):
        pokemon = sys.stdin.readline().strip()
        poketmons_number[i + 1] = pokemon
        poketmons_name[pokemon] = i + 1

    for _ in range(M):
        q = sys.stdin.readline().strip()
        if q.isdecimal():
            print(poketmons_number.get(int(q)))
        else:
            print(poketmons_name.get(q))