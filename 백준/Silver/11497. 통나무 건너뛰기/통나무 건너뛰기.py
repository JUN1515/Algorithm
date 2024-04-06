import sys
input = sys.stdin.readline

def solution():
    N = int(input().strip())
    arr = list(map(int, input().strip().split()))
    arr.sort()
    max_val = arr[1] - arr[0]
    for i in range(3, N, 2):
        max_val = max(max_val, arr[i] - arr[i - 2])

    for i in range(2, N, 2):
        max_val = max(max_val, arr[i] - arr[i - 2])
    print(max_val)


T = int(input())
for _ in range(T):
    solution()