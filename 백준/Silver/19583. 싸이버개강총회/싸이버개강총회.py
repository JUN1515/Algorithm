import sys
input = sys.stdin.readline

def time_compare(t1, t2):
    m1 = int(t1[:2]) * 60 + int(t1[3:])
    m2 = int(t2[:2]) * 60 + int(t2[3:])
    return True if m1 >= m2 else False

def solution():

    S, E, Q = input().strip().split()
    check = {}

    while (log := sys.stdin.readline()):
        time, name = log.strip().split()

        if time_compare(S, time):
            check[name] = 0

        else:
            if time_compare(time, E) and time_compare(Q, time):
                if name in check:
                    check[name] += 1

    answer = 0
    for val in check.values():
        if val:
            answer += 1
    print(answer)


solution()