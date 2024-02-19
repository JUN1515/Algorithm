import sys
input = sys.stdin.readline

def solution():
    N = int(input())

    dp = [0] * (N + 1)
    dp[1] = 1
    if N == 1:
        return dp[1]

    dp[2] = 1
    if N > 2:
        for i in range(3, N + 1):
            dp[i] = dp[i - 2] + dp[i - 3]

    return dp[N]


T = int(input())
for _ in range(T):
    print(solution())