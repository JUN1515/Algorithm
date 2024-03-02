import sys
input = sys.stdin.readline

def solution():
    word1 = input().strip()
    word2 = input().strip()

    n1, n2 = len(word1), len(word2)
    dp = [0] * n2

    for i in range(n1):
        cnt = 0
        for j in range(n2):
            if cnt < dp[j]:
                cnt = dp[j]
            elif word1[i] == word2[j]:
                dp[j] = cnt + 1
    print(max(dp))


solution()