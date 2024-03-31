import sys
input = sys.stdin.readline

def solution():
    N, K = map(int, input().split())
    arr = list(map(int, input().strip().split()))

    diff = []
    for i in range(1, N):
        diff.append(arr[i] - arr[i-1])
    diff.sort(reverse=True)
    print(sum(diff[K-1:]))


solution()