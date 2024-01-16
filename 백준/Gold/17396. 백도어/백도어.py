import sys
from heapq import *

def Dijkstra(N, start, end):
    global G, passable
    INF = int(1e12)

    distance = [INF] * N
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
    return -1

input = sys.stdin.readline

# N: 분기점의 수(노드의 수), M: 간선의 수
N, M = map(int, input().split())

# 각 분기점 지날 수 있는 여부, # 0은 통과 가능, 1은 통과 불가
not_passable = list(map(int, input().split()))
not_passable[N-1] = 0   # 단, N-1은 통과 가능

# 간선 정보 (양방향)
G = [{} for _ in range(N)]
for _ in range(M):
    a, b, t = map(int, input().split())
    if not_passable[a] or not_passable[b]: continue # 지나갈 수 없는 경우
    G[a][b] = t
    G[b][a] = t

print(Dijkstra(N, 0, N-1))