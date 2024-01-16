import sys
from heapq import *

def Dijkstra(N, start, end):
    global INF, G, P

    distance = [INF] * (N + 1)
    distance[start] = 0

    heap = [(0, start)]
    heapify(heap)

    while heap:
        current_dist, v = heappop(heap)

        if distance[v] < current_dist: continue

        if v == end:
            return distance

        for w, dist in G[v].items():
            next_dist = current_dist + dist

            if distance[w] > next_dist:
                distance[w] = next_dist
                heappush(heap, (next_dist, w))
    return distance


input = sys.stdin.readline
INF = int(1e10)

# V: 정점의 개수, E: 간선의 개수, P: 건우의 위치
V, E, P = map(int, input().split())

# 간선 정보
G = [{} for _ in range(V + 1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    G[a][b] = c
    G[b][a] = c

arr = Dijkstra(V, 1, V)
arr2 = Dijkstra(V, P, V)
if arr[V] >= arr[P] + arr2[V]:
    print("SAVE HIM")
else:
    print("GOOD BYE")