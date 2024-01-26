import sys
from collections import deque

def topology_sort(find_node):
    global indegree, delays, graph

    Q = deque([i for i in range(1, N + 1) if indegree[i] == 0]) # 큐 정의
    result = [0] * (N + 1)

    for i in Q:
        result[i] = delays[i]
        if i == find_node:
            return result[i]

    for _ in range(N):
        v = Q.popleft()

        for w in graph[v]:
            result[w] = max(result[w], result[v] + delays[w])
            indegree[w] -= 1

            if indegree[w] == 0:
                if w == find_node:
                    return result[w]

                Q.append(w)


input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N, K = map(int, input().split())        # 정점의 수, 규칙의 수
    indegree = [0] * (N + 1)                # 진입 차수 배열

    delays = [0] + list(map(int, input().split()))

    graph = [[] for _ in range(N + 1)]
    for _ in range(K):
        X, Y = map(int, input().split())    # X -> Y
        graph[X].append(Y)
        indegree[Y] += 1
    W = int(input())

    print(topology_sort(W))