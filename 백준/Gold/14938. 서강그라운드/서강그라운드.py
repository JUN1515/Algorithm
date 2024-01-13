import sys
from heapq import *

def Dijkstra(N, start):
    global items, G, m
    INF = 1e9
    distance = [INF] * (N + 1)
    item_check = [False] * (N + 1)
    item_check[start] = True

    heap = [(0, start)]
    heapify(heap)

    while heap:
        current_dist, v = heappop(heap)

        if distance[v] < current_dist: continue

        for w, dist in G[v].items():
            next_dist = current_dist + dist
            if (distance[w] > next_dist) and (m >= next_dist):
                distance[w] = next_dist
                # 다음 경로의 아이템 체크
                item_check[w] = True
                heappush(heap, (next_dist, w))
    total_item = 0
    for i in range(1, n + 1):
        if item_check[i]:
            total_item += items[i]
    return total_item

input = sys.stdin.readline

# n: 노드, m: 수색범위, r: 간선
n, m, r = map(int, input().split())

# 각 구역에 있는 아이템의 수
items = [0] + list(map(int, input().split()))

# 간선 정보 저장
G = [{} for _ in range(n + 1)]
for _ in range(r):
    # 지역번호: a, b, 길의 길이: l
    a, b, l = map(int, input().split())

    if b in G[a]:
        if G[a][b] <= l: continue

    # 양방향
    G[a][b] = G[b][a] = l

# 각 구역에 대해 반복문을 통해 최대 아이템 개수 확인
max_item = 0
for i in range(1, n+1):
    temp_item = Dijkstra(n, i)
    if max_item < temp_item:
        max_item = temp_item
print(max_item)