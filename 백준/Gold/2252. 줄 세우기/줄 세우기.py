import sys
from collections import deque

def topology_sort(n):
    global graph, indegree
    Q = deque([n])

    result = []
    while Q:
        v = Q.popleft()
        result.append(v)

        for w in graph[v]:
            indegree[w] -= 1
            if indegree[w] == 0:
                Q.append(w)

    return result

input = sys.stdin.readline
# 정점의 수, 비교 횟수
N, M = map(int, input().split())
indegree = [0] * (N + 1)

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, input().split())    # A -> B
    graph[A].append(B)
    indegree[B] += 1

arr = []
for i in range(1, N + 1):
    if indegree[i] == 0:
        arr.append(i)

answer = []
for elm in arr:
    temp = topology_sort(elm)
    answer.extend(temp)
print(*answer)