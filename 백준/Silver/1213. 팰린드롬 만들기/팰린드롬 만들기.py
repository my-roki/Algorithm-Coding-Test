import sys
from collections import defaultdict


def make_palindrom(alphabets: dict) -> str or int:
    # key 내림차순 정렬 -> 사전순으로 앞서는 펠린트롬
    alphabets = sorted(alphabets.items(), reverse=True)

    cond = 1
    result = ""
    for k, v in alphabets:
        # 홀수개인 문자는 무조건 가운데에 와야 합니다.
        if v % 2 == 1:
            cond -= 1

            # 사전순으로 앞서는 펠린드롬을 만들기 위한 조건
            # 홀수개 알파벳이 사전순으로 앞선 알파벳이면, 중간에 1개만 넣고 나머지는 양 끝에 누적
            if len(result) > 0:
                result = result[: int(len(result) / 2)] + k + result[int(len(result) / 2) :]
                v -= 1
            else:
                result = result[: int(len(result) / 2)] + k * v + result[int(len(result) / 2) :]
                continue
            
        result = k * int(v / 2) + result + k * int(v / 2)

        # 홀수개인 알파벳이 2개 이상이면 팰린드롬이 성립하지 않으므로 "I'm Sorry Hansoo"를 return.
        if cond < 0:
            return "I'm Sorry Hansoo"

    return result


if __name__ == "__main__":
    word = sys.stdin.readline().strip()

    alphabets = defaultdict(int)
    for i in word:
        alphabets[i] += 1

    print(make_palindrom(alphabets))
