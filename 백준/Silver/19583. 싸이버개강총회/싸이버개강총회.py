import sys
input = sys.stdin.readline

def solution():

    S, E, Q = input().strip().split()
    check = set()
    answer = 0

    while (log := sys.stdin.readline()):
        time, name = log.strip().split()

        if time <= S:
            check.add(name)

        elif E <= time <= Q:
            if name in check:
                check.remove(name)
                answer += 1

    print(answer)


solution()