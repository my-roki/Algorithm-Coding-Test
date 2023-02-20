from collections import Counter


def solution(X: str, Y: str) -> str:
    xy_counters = Counter(X) & Counter(Y)

    if len(xy_counters) == 0:
        return "-1"

    intersections = sorted(list(xy_counters.elements()), reverse=True)

    return "0" if intersections[0] == "0" else "".join(intersections)