import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    arr = [[0] + list(map(int, input().strip().split())) for _ in range(2)]

    dp = [[0] * (n + 1) for _ in range(2)]
    dp[0][1] = arr[0][1]
    dp[1][1] = arr[1][1]

    if n != 1:
        for i in range(2, n + 1):
            dp[0][i] = max(dp[1][i - 1], dp[1][i - 2]) + arr[0][i]
            dp[1][i] = max(dp[0][i - 1], dp[0][i - 2]) + arr[1][i]
    return max(dp[0][n], dp[1][n])


T = int(input())
for _ in range(T):
    print(solution())