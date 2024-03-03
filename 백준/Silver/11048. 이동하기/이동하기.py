def solution():
    N, M = map(int, input().strip().split())
    arr = [[0] * (M + 1)] + [[0] + list(map(int, input().strip().split())) for _ in range(N)]
    dp = [[0] * (M + 1) for _ in range(N + 1)]

    for r in range(1, N + 1):
        for c in range(1, M + 1):
            dp[r][c] = arr[r][c] + max(dp[r - 1][c], dp[r][c - 1], dp[r - 1][c - 1])
    print(dp[N][M])


solution()