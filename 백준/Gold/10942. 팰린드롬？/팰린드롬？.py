# dp의 각 요소는 펠린드롬의 시작 위치에 해당.
# dp[i]의 i는 시작지점과 끝지점의 합을 의미 |(ex i가 4이면, 1 3, 2 2 가 될 수 있음)
# i = s + e일 때, dp[i] < s 이면 s -> e 는 펠린드롬이다.
# 만일 i가 4이고, dp[4] = 1 이면, 2 2 는 펠린드롬이지만 1 3 은 펠린드롬이 아님
import sys

def solution():
    input = sys.stdin.readline
    N = int(input())
    arr = [0] + list(map(int, input().split()))
    dp = [0] * (N * 2 + 1)

    for i in range(N * 2 + 1):
        s = e = i // 2
        e += i & 1  # i가 홀수이면 e에 +1 해주기

        while s > 0 and e <= N and arr[s] == arr[e]:
            s -= 1
            e += 1
        dp[i] = s   # s + 1 부터 펠린드롬이 가능 

    M = int(input())
    result = [0] * M
    for i in range(M):
        S, E = map(int, input().split())
        if dp[S + E] < S:
            result[i] = 1

    for i in range(M):
        print(result[i])


solution()