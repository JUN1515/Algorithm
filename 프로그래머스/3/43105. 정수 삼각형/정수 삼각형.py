# dp문제
# dp[n][i] = max(dp[n+1][i], dp[n+1][i+1]) + triangle[n][i] 

def solution(triangle):
    N = len(triangle)
    
    # dp 배열 생성
    dp = [[0] * (i + 1) for i in range(N + 1)]
    
    for n in range(N - 1, -1, -1):
        for i in range(n + 1):
            dp[n][i] = max(dp[n + 1][i], dp[n + 1][i + 1]) + triangle[n][i]
    
    return dp[0][0]