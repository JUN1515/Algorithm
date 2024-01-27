import sys
from collections import deque

def topology_sort():
    N, M = map(int, input().split())
    indegree = [0] * (N + 1)

    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        c, *G = list(map(int, input().split()))
        for i in range(1, c):
            graph[G[i - 1]].append(G[i]) # i-1 -> i
            indegree[G[i]] += 1

    Q = deque([i for i in range(1, N + 1) if indegree[i] == 0])
    visited = [0] * (N + 1)
    result = []

    while Q:
        v = Q.popleft()

        if visited[v] == 1:
            return 0
        visited[v] = 1
        result.append(v)

        for w in graph[v]:
            indegree[w] -= 1
            if indegree[w] == 0:
                Q.append(w)

    if len(result) == N:
        return result
    return 0

input = sys.stdin.readline
answer = topology_sort()
if answer == 0:
    print(0)
else:
    for ans in answer:
        print(ans)