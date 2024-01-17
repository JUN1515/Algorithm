import sys
from heapq import *

def Dijkstra(N, start):
    global INF, G, result
    distance = [INF] * (N + 1)
    distance[start] = 0

    path = [0] * (N + 1)
    path[start] = start

    heap = [(0, start)]
    heapify(heap)

    while heap:
        current_dist, v = heappop(heap)
        if distance[v] < current_dist: continue

        for w, dist in G[v].items():
            next_dist = current_dist + dist
            if distance[w] > next_dist:
                distance[w] = next_dist
                path[w] = v
                heappush(heap, (next_dist, w))

    for i in range(1, N + 1):
        result[start][i] = path_check(path, start, i)
    result[start][start] = '-'


def path_check(path, start, x):
    if path[x] != start:
        return path_check(path, start, path[x])
    return x


input = sys.stdin.readline
INF = int(1e9)

# n: 정점의 개수, m: 간선의 개수
n, m = map(int, input().split())

# 간선 정보, 무방향
G = [{} for _ in range(n + 1)]
for _ in range(m):
    a, b, t = map(int, input().split())
    if b in G[a]:
        if G[a][b] <= t: continue
    G[a][b] = t
    G[b][a] = t

result = [['-'] * (n + 1) for _ in range(n + 1)]
for i in range(1, n+1):
    Dijkstra(n, i)

for i in range(1, n+1):
    print(*result[i][1:])