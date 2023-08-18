def solution(s: str) -> list:
    answer = []

    a = s[2:-2].split("},{")
    a.sort(key=len)

    for i in a:
        b = i.split(",")
        for j in b:
            if int(j) not in answer:
                answer.append(int(j))

    return answer