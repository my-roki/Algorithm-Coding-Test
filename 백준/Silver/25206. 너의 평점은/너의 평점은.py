import sys

grades = {"A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0, "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0}
total_grade = 0
total_point = 0
for line in sys.stdin.readlines():
    [_, point, grade] = line.split()
    if grade == "P":
        continue

    point = float(point)
    total_grade += grades.get(grade) * point
    total_point += point

print(round(total_grade / total_point, 6))
