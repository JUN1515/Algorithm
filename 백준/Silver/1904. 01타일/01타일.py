def solution():
    N = int(input())
    dp = [0] * (N + 1)
    dp[1] = 1
    if N == 1: return dp[N]

    dp[2] = 2
    if N == 2: return dp[N]

    for i in range(3, N + 1):
        dp[i] = (dp[i - 2] + dp[i - 1]) % 15746
    return dp[N]


print(solution())