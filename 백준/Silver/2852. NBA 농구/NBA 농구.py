import sys


def time_to_sec(str_time):
    m, s = str_time.split(":")
    return int(m) * 60 + int(s)


def sec_to_time(sec_time):
    m = sec_time // 60
    s = sec_time % 60
    return "{:02d}:{:02d}".format(m, s)


N = sys.stdin.readline().rstrip()


before = 0
a_score = 0
b_score = 0
a_time = 0
b_time = 0

for i in range(int(N)):
    N, M = map(str, sys.stdin.readline().split())
    M = time_to_sec(M)
    if a_score > b_score:
        a_time += M - before
    elif a_score < b_score:
        b_time += M - before
    else:
        pass

    if N == "1":
        a_score += 1
    else:
        b_score += 1

    before = M

if a_score > b_score:
    a_time += time_to_sec("48:00") - before
elif a_score < b_score:
    b_time += time_to_sec("48:00") - before
else:
    pass


print(sec_to_time(a_time))
print(sec_to_time(b_time))
