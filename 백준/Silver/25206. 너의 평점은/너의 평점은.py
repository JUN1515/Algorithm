import sys
input = sys.stdin.readline
def solution():
    dic = {"A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0,
           "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0,
           "F": 0.0, "P": -1}

    cnt = total = 0
    for i in range(20):
        name, grade, rank = input().strip().split()
        grade = int (float (grade))
        if dic[rank] < 0:
            continue
        total += (grade * dic[rank])
        cnt += grade
    print(total / cnt)


solution()