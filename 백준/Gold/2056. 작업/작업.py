import sys
from collections import deque

input = sys.stdin.readline
N = int(input())            # 정점의 수
indegree = [0] * (N + 1)
times = [0] * (N + 1)       # 작업 시간 배열

graph = [[] for _ in range(N + 1)]
for w in range(1, N + 1):
    temp = list(map(int, input().split()))
    times[w] = temp[0]                  # 작업 시간
    indegree[w] = temp[1]

    for v in range(2, 2 + temp[1]):     # v -> w
        graph[temp[v]].append(w)

Q = deque()
for i in range(1, N + 1):
    if indegree[i] == 0:
        Q.append(i)

result = [0] * (N + 1)

for _ in range(N):
    v = Q.popleft()
    result[v] += times[v]

    for w in graph[v]:
        indegree[w] -= 1
        result[w] = max(result[w], result[v])
        if indegree[w] == 0:
            Q.append(w)
print(max(result))