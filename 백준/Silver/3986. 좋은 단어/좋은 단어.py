import sys


if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())
    cnt = 0
    for i in range(N):
        word = sys.stdin.readline().strip()
        bucket = []
        for w in word:
            # bucket이 비워져 있으면 비교 대상이 없으므로 bucket에 w를 담고 다음 문자와 비교를 한다.
            if len(bucket) == 0:
                bucket.append(w)
                continue

            candidate = bucket.pop()

            # bucket의 마지막 단어와 비교되는 w가 같다면 교차하지 않고 선을 그을 수 있다.
            if candidate == w:
                continue
            # bucket의 마지막 단어와 비교되는 w가 다르면 필연적으로 교차가 생기기 때문에 다음 문자를 기약해야 한다.
            else:
                bucket.append(candidate)
                bucket.append(w)

        # 모든 문자를 비교하고 bucket에 문자가 남아있다는 뜻은 교차하는 문자가 필연적으로 생길수 밖에 없다는 뜻.
        if len(bucket) == 0:
            cnt += 1
    print(cnt)
