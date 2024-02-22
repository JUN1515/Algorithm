def solution():
    N = int(input())
    dp = [[0] * 10 for _ in range(N + 1)]
    d = 1000000000
    if N == 1:
        return 9

    for i in range(1, 10):
        dp[1][i] = 1

    for n in range(2, N + 1):
        for i in range(0, 10):
            if i == 0:
                dp[n][0] = dp[n - 1][1] % d
            elif i == 9:
                dp[n][9] = dp[n - 1][8] % d
            else:
                dp[n][i] = (dp[n - 1][i - 1] + dp[n - 1][i + 1]) % d

    return sum(dp[N]) % d


print(solution())