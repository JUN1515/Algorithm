import sys
input = sys.stdin.readline

n = int(input())    # n은 배열 크기 (n x n)
arr = [list(map(int, input().split())) for _ in range(n)]   # 배열 정보
dp = [[0] * n for _ in range(n)]

# dp[0][x]
for c in range(1, n):
    dp[0][c] = dp[0][c-1] + (arr[0][c] + 1 - arr[0][c-1] if arr[0][c] >= arr[0][c-1] else 0)

# dp[x][0]
for r in range(1, n):
    dp[r][0] = dp[r-1][0] + (arr[r][0] + 1 - arr[r-1][0] if arr[r][0] >= arr[r-1][0] else 0)

for r in range(1, n):
    for c in range(1, n):
        dp[r][c] = min(
            dp[r-1][c] + (arr[r][c] + 1 - arr[r-1][c] if arr[r][c] >= arr[r-1][c] else 0),
            dp[r][c-1] + (arr[r][c] + 1 - arr[r][c-1] if arr[r][c] >= arr[r][c-1] else 0)
        )
print(dp[n-1][n-1])