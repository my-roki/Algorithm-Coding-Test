import sys
from typing import List


def get_max_temperature(temperatures: List[int], K: int) -> List[int]:
    result = [sum(temperatures[:K])]
    for t in range(len(temperatures) - K):
        result.append(result[t] - temperatures[t] + temperatures[t + K])

    return result


if __name__ == "__main__":
    _, K = map(int, sys.stdin.readline().strip().split())
    temperatures = list(map(int, sys.stdin.readline().strip().split()))

    print(max(get_max_temperature(temperatures, K)))