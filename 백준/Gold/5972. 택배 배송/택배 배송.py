import sys
from heapq import *

def Dijkstra(N, start, end):
    global G
    INF = int(1e9)

    distance = [INF] * (N + 1)
    distance[start] = 0

    # 시작 시 비용, 출발 비용
    heap = [(0, start)]
    heapify(heap)

    # 다익스트라 알고리즘
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

# N개의 헛간 (노드), M개 의 간선(양뱡향)
N, M = map(int, input().split())

# 간선 정보, key는 노드, value는 간선
G = [{} for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())

    # 두 개의 노드느 하나 이상의 길로 연결되어 있을 수 도 있기에, 최소 비용의 길만 남겨둠
    if b in G[a]:
        if G[a][b] <= c: continue

    # 양방향
    G[a][b] = c
    G[b][a] = c

print(Dijkstra(N, 1, N))