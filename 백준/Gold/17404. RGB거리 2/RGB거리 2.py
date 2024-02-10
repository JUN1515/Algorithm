import sys
input = sys.stdin.readline

def solution():

    def func(s):
        INF = 1001
        dp = [[0] * 3 for _ in range(N)]

        # 첫 번째 위치를 고정해서 시작, 나머지는 INF 값으로
        for i in range(3):
            dp[0][i] = arr[0][i] if i == s else INF

        # 두 번째 집부터 N - 1 번째 집까지, 이전 집 색칠 비용 중 최소를 현재 집 색칠 비용에 더함
        # 이때, 이전 집과 색깔이 겹치지 않도록 해야 함.
        for i in range(1, N - 1):
            dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + arr[i][0]
            dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + arr[i][1]
            dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + arr[i][2]

        # 마지막 위치의 경우, 이전 집 색깔과 첫번째 집 색깔을 고려해야 함.
        for i in range(3):
            if i != s:
                dp[N - 1][i] = min(dp[N - 2][i - 1], dp[N - 2][(i + 1) % 3]) + arr[N - 1][i]
            else:
                dp[N - 1][i] = INF * N

        return min(dp[N - 1])


    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    min_val = 1001 * N
    for i in range(3):
        min_val = min(min_val, func(i))
    print(min_val)


solution()