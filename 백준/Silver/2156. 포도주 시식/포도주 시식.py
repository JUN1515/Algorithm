import sys
input = sys.stdin.readline

def solution():
    N = int(input())
    arr = [0] + [int(input()) for _ in range(N)]
    dp = [0] * (N + 1)

    dp[1] = arr[1]
    if N == 1:
        return dp[1]

    dp[2] = arr[1] + arr[2]
    if N == 2:
        return dp[2]

    if N > 2:
        for i in range(3, N + 1):
            dp[i] = max(dp[i - 3] + arr[i - 1] + arr[i], dp[i - 2] + arr[i], dp[i - 1])

    return dp[N]


print(solution())