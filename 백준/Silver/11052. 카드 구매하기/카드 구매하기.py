import sys
input = sys.stdin.readline

def solution():
    N = int(input())
    dp = [0] + list(map(int, input().strip().split()))
    if N == 1:
        return dp[N]

    for i in range(2, N + 1):
        for j in range(i//2 + 1):
            dp[i] = max(dp[i - j] + dp[j], dp[i])
    return dp[N]


print(solution())