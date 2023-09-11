from typing import List
from collections import defaultdict


def solution(genres: List[str], plays: List[int]) -> List[int]:
    answer = []
    ranks = defaultdict(int)

    for i in range(len(genres)):
        ranks[genres[i]] += plays[i]

    ranks = sorted(ranks.items(), key=lambda x: x[1], reverse=True)

    for rank in ranks:
        playlist = [[i, plays[i]] for i in range(len(genres)) if rank[0] == genres[i]]
        playlist.sort(key=lambda x: x[1], reverse=True)

        answer.append(playlist[0][0])
        if len(playlist) >= 2:
            answer.append(playlist[1][0])

    return answer


if __name__ == "__main__":
    print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))  # [4, 1, 3, 0]
