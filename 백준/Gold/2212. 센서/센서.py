import sys
input = sys.stdin.readline

def solution():
    N = int(input().strip())
    K = int(input().strip())
    arr = list(map(int, input().strip().split()))
    arr.sort()
    diff = []
    for i in range(1, N):
        diff.append(arr[i] - arr[i - 1])
    diff.sort(reverse=True)
    print(sum(diff[K -1:]))


solution()