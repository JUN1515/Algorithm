import sys
from heapq import *

def Dijkstra(N, start):
    global INF, G, friend_position, min_node, min_distance

    distance = [INF] * (N + 1)
    distance[start] = 0

    heap = [(0, start)]
    heapify(heap)

    while heap:
        current_dist, v = heappop(heap)
        if distance[v] < current_dist: continue

        for w, dist in G[v].items():
            next_dist = current_dist + dist
            if distance[w] > next_dist:
                distance[w] = next_dist
                heappush(heap, (next_dist, w))

    total_dist = 0
    for node in friend_position:
        total_dist += distance[node]

    if min_distance > total_dist:
        min_node, min_distance = start, total_dist
    elif min_distance == total_dist:
        min_node = min(min_node, start)


input = sys.stdin.readline
INF = int(1e9)
T = int(input())

for _ in range(T):

    # N: 정점의 개수, M: 간선의 개수
    N, M = map(int, input().split())

    # 간선 정보, a - b 이동 거리 c
    G = [{} for _ in range(N + 1)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        G[a][b] = c
        G[b][a] = c

    K = int(input())
    friend_position = list(map(int, input().split()))

    # 각 방을 목적지라 생각하고 반복문 수행
    min_node, min_distance = N, INF + 1
    for i in range(1, N + 1):
        Dijkstra(N, i)
    print(min_node)