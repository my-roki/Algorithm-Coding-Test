from typing import List
from collections import defaultdict


def prev_solution(info: List[str], query: List[str]) -> List[int]:
    answer = []
    info = [i.split() for i in info]
    query = [q.split() for q in query]

    for q in query:
        count = 0
        for i in info:
            if (
                (q[0] == "-" or q[0] == i[0])
                and (q[2] == "-" or q[2] == i[1])
                and (q[4] == "-" or q[4] == i[2])
                and (q[6] == "-" or q[6] == i[3])
                and int(q[7]) <= int(i[4])
            ):
                count += 1
        answer.append(count)
    return answer


def solution(info: List[str], query: List[str]) -> List[int]:
    answer = []
    info = [i.split() for i in info]
    query = [q.split() for q in query]

    # 모든 조건의 경우의 수를 딕셔너리에 저장
    info_dict = defaultdict(list)
    for i in info:
        for a in range(2):
            for b in range(2):
                for c in range(2):
                    for d in range(2):
                        cond = f"{i[0] if a == 0 else '-'} {i[1] if b == 0 else '-'} {i[2] if c == 0 else '-'} {i[3] if d == 0 else '-'}"
                        info_dict[cond].append(int(i[4]))

    for key in info_dict.keys():
        info_dict[key].sort()

    for q in query:
        count = 0
        cond = f"{q[0]} {q[2]} {q[4]} {q[6]}"
        if cond in info_dict:
            data = info_dict[cond]

            # binary search
            start = binary_search(data, int(q[7]))
            count = len(data) - start

        answer.append(count)

    return answer


def binary_search(data: List[int], target: int, is_sorted: bool = True) -> int:
    if not is_sorted:
        data.sort()
    start, end = 0, len(data)
    while start < end:
        mid = (start + end) // 2
        if data[mid] >= target:
            end = mid
        else:
            start = mid + 1
    return start


if __name__ == "__main__":
    print(
        solution(
            [
                "java backend junior pizza 150",
                "python frontend senior chicken 210",
                "python frontend senior chicken 150",
                "cpp backend senior pizza 260",
                "java backend junior chicken 80",
                "python backend senior chicken 50",
            ],
            [
                "java and backend and junior and pizza 100",
                "python and frontend and senior and chicken 200",
                "cpp and - and senior and pizza 250",
                "- and backend and senior and - 150",
                "- and - and - and chicken 100",
                "- and - and - and - 150",
            ],
        )
    )  # [1,1,1,1,2,4]
