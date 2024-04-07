import sys
input = sys.stdin.readline

def solution():
    N = int(input().strip())
    p = [0, 1]

    while p[-1] < N:
        p.append(p[-1] + p[-2])

    answer = []
    for i in range(len(p)-1, 0, -1):
        if N < p[i]:
            continue
        answer.append(p[i])

        if N == p[i]:
            break
        N -= p[i]

    answer.sort()
    print(*answer)


T = int(input().strip())
for _ in range(T):
    solution()