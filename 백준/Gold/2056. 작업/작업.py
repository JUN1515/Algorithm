import sys

input = sys.stdin.readline
N = int(input())
dp = [0] * (N + 1)

for n in range(1, N + 1):
    time, indegree, *G = list(map(int, input().split()))
    dp[n] = time + (max([dp[i] for i in G]) if indegree else 0)
print(max(dp))