import sys;
from heapq import *

def Dijkstra():
    global G, D
    INF = int(1e10)
    distance = [INF] * (D + 1)
    distance[0] = 0

    heap = [(0, 0)]
    heapify(heap)

    while heap:
        current_dist, v = heappop(heap)
        if distance[v] < current_dist: continue

        if v == D:
            return current_dist

        for w, dist in G[v].items():
            next_dist = current_dist + dist
            if distance[w] > next_dist:
                distance[w] = next_dist
                heappush(heap, (next_dist, w))


input = sys.stdin.readline

N, D = map(int, input().split())    # N: 지름길의 개수, D: 고속도로의 길이

# 가능한 간선 정보 정리
shortcut = [list(map(int, input().split())) for _ in range(N)]  # 지름길 정보
load = [[0, D, D]]                                              # 초기 고속도로 비용

for i in range(N):
    start1, end1, dist1 = shortcut[i]                   # 지름길 시작점, 도착점, 지름길 거리
    if end1 > D: continue                               # 지름길의 도착점 > 고속도록의 도착점 이면 제거

    if dist1 > end1 - start1:                           # 지름길이 더 긴 경우,
        dist1 = end1 - start1                           # 지름길 비용을 고속도로 비용으로 변경후
    load.append([start1, end1, dist1])                  # load 배열에 추가


    if start1 != 0:
        load.append([0, start1, start1])                # 고속도로의 시작점 -> 다른 지름길의 시작점

    if end1 != D:
        load.append([end1, D, D - end1])                # 다른 지름길의 도착점 -> 고속도로의 도착점

    for j in range(N):
        if i == j: continue
        start2 = shortcut[j][0]
        if end1 < start2:                               # 지름길의 도착점 < 다른 지름길의 시작점
            load.append([end1, start2, start2 - end1])  # 지름길의 도착점 -> 다른 지름길의 시작점

G = [{} for _ in range(D + 1)]  # D <= 10000
for a, b, d in load:            # a -> b 로 이동하는 비용 d
    if b in G[a]:
        if G[a][b] <= d: continue
    G[a][b] = d

print(Dijkstra())