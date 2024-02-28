def solution():
    N = int(input())
    dp = [[0] * 11 for _ in range(N + 1)]

    if N == 1: return 10
    for i in range(10):
        dp[1][i] = 1

    for n in range(2, N + 1):
        for i in range(10):
            for j in range(i, 10):
                dp[n][i] += dp[n - 1][j]

    return sum(dp[N]) % 10007


print(solution())