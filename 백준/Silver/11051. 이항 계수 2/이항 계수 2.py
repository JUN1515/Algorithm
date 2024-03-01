def solution():
    N, K = map(int, input().strip().split())
    dp = [[0] * (K + 1) for _ in range(N + 1)]

    if N == 1 or K == 0:
        return 1

    for i in range(1, N + 1):
        dp[i][0] = 1
    dp[1][1] = 1

    for i in range(2, N + 1):
        for j in range(1, i + 1):
            if j > K: break
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
    return dp[N][K]


print(solution() % 10007)