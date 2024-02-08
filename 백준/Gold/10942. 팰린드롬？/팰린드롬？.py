import sys

def solution():
    input = sys.stdin.readline
    N = int(input())                        # 수열의 크기
    arr = list(map(int, input().split()))
    dp = [[False] * N for _ in range(N)]    # dp[r][c]는 r부터 c까지 수의 펠린드롬 여부

    # Case 1. i -> i 의 경우, 모두 펠린드롬
    for i in range(N):
        dp[i][i] = True

    if N > 1:
        # Case 2. i -> i + 1 의 경우, 양 끝의 두 수가 같아야 펠린드롬
        for i in range(N - 1):
            if arr[i] == arr[i + 1]:
                dp[i][i+1] = True

    if N > 2:
        # Case 3. i -> i + k (2 <= k < N) 의 경우,
        # 양 끝의 수(i, i + k)가 같고, 양 끝 안 쪽의 수(i + 1 -> i + k - 1) 들이 펠린드롬이면, 펠린드롬
        for k in range(2, N):
            for i in range(N - k):
                if arr[i] == arr[i + k] and dp[i + 1][i + k - 1]:
                    dp[i][i + k] = True

    M = int(input())
    result = [0] * M
    for i in range(M):
        S, E = map(int, input().split())
        if dp[S-1][E-1]:
            result[i] = 1

    for i in range(M):
        print(result[i])


solution()