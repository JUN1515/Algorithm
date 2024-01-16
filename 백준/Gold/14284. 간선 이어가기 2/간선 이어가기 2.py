import sys
from heapq import *

def Dijkstra(N, start, end):
    global G
    INF = int(1e10)
    distance = [INF] * (N + 1)
    distance[start] = 0

    heap = [(0, start)]
    heapify(heap)

    while heap:
        current_dist, v = heappop(heap)
        if distance[v] < current_dist: continue

        if v == end:
            return current_dist

        for w, dist in G[v].items():
            next_dist = current_dist + dist
            if distance[w] > next_dist:
                distance[w] = next_dist
                heappush(heap, (next_dist, w))


input = sys.stdin.readline

# n: 정점의 개수, m: 간선의 개수
n, m = map(int, input().split())

# 간선 정보 (무방향), a - b의 가중치 c
G = [{} for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int ,input().split())
    if b in G[a]:
        if G[a][b] <= c: continue
    G[a][b] = c
    G[b][a] = c

s, t = map(int, input().split())
print(Dijkstra(n, s, t))