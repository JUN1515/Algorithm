import sys
input = sys.stdin.readline

def solution():
    N = int(input().strip())
    arr = [list(map(int, input().strip().split())) for _ in range(N)]
    arr.sort(key=lambda x: (x[0], x[1]))

    time = -1
    for i in range(N):
        if arr[i][0] >= time:
            time = arr[i][0] + arr[i][1]
        else:
            time += arr[i][1]
    print(time)


solution()