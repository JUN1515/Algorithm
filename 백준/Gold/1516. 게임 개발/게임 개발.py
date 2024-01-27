import sys
from collections import deque

input = sys.stdin.readline
N = int(input())   # 정점의 수
indegree = [0] * (N + 1)

times = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]
for i in range(1, N + 1):
    t, *G = map(int, input().split())
    times[i] = t
    n_count = len(G) - 1
    indegree[i] = n_count
    for j in range(n_count):
        graph[G[j]].append(i)      # G[j] -> i

Q = deque()
result = [0] * (N + 1)

for i in range(1, N + 1):
    if indegree[i] == 0:
        result[i] = times[i]
        Q.append(i)

while Q:
    v = Q.popleft()

    for w in graph[v]:
        indegree[w] -= 1
        result[w] = max(result[w], result[v] + times[w])

        if indegree[w] == 0:
            Q.append(w)

for i in range(1, N + 1):
    print(result[i])