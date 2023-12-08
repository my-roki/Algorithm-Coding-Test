import sys


def min_to_sec(m: str | int, s: str | int) -> int:
    return int(m) * 60 + int(s)


def sec_to_min(s: int) -> str:
    return f"{str(s//60).zfill(2)}:{str(s % 60).zfill(2)}"


if __name__ == "__main__":
    N = int(sys.stdin.readline())

    # team = [score, win time]
    team_1 = [0, 0]
    team_2 = [0, 0]
    prev = 0
    for _ in range(N):
        win, goal_time = sys.stdin.readline().split()
        goal_time_sec = min_to_sec(goal_time[:2], goal_time[3:])

        # 시간 정산
        if team_1[0] > team_2[0]:
            team_1[1] += goal_time_sec - prev
        elif team_2[0] > team_1[0]:
            team_2[1] += goal_time_sec - prev
        else:
            pass
        prev = goal_time_sec

        # 골 정산
        if win == "1":
            team_1[0] += 1
        else:
            team_2[0] += 1
    else:
        # 종료시 시간 정산
        if team_1[0] > team_2[0]:
            team_1[1] += min_to_sec(48, 0) - prev
        elif team_2[0] > team_1[0]:
            team_2[1] += min_to_sec(48, 0) - prev
        else:
            pass

    print(sec_to_min(team_1[1]))
    print(sec_to_min(team_2[1]))