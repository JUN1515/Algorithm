import sys
from collections import deque

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    # K는 테스트 케이스 번호, M은 노드의 수, P는 간선의 수
    K, M, P = map(int, input().split())
    indegree = [0] * (M + 1)

    graph =[[] for _ in range(M + 1)]
    for _ in range(P):
        A, B = map(int, input().split()) # A -> B
        graph[A].append(B)
        indegree[B] += 1

    Q = deque()
    dp = [[0, 0] for _ in range(M + 1)]     # [현재 노드의 순서, 현재 노드의 순서와 동일한 선행 노드의 개수]
    for i in range(1, M + 1):
        if indegree[i] == 0:
            Q.append(i)
            dp[i][0] = 1

    for _ in range(M):
        v = Q.popleft()

        for w in graph[v]:
            indegree[w] -= 1
            if indegree[w] == 0:
                Q.append(w)

            if dp[w][0] > dp[v][0]: continue
            dp[w] = [dp[v][0] + 1, 0] if dp[w][0] == dp[v][0] and dp[w][1] else [dp[v][0], 1]

    print(K, max(dp, key=lambda x: x[0])[0])