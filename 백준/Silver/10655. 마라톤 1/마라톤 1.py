import sys
input = sys.stdin.readline

def solution():
    N = int(input().strip())
    arr = [tuple(map(int, input().strip().split())) for _ in range(N)]

    diff_1 = [0] * (N - 1)
    for i in range(N - 1):
        diff_1[i] = abs(arr[i + 1][0] - arr[i][0]) + abs(arr[i + 1][1] - arr[i][1])

    max_reduction_path = 0
    for i in range(N - 2):
        jump_path = abs(arr[i + 2][0] - arr[i][0]) + abs(arr[i + 2][1] - arr[i][1])
        default_path = diff_1[i] + diff_1[i + 1]
        if max_reduction_path < (reduction_path := default_path - jump_path):
            max_reduction_path = reduction_path
    answer = sum(diff_1) - max_reduction_path
    print(answer)


solution()