import sys
from heapq import *

def Dijkstra(N, start):
    global INF, G
    distance = [INF] * (N + 1)
    distance[start] = 0

    heap = [(0, start)]
    heapify(heap)

    # 다익스트라 알고리즘
    while heap:
        current_dist, v = heappop(heap)

        if distance[v] < current_dist: continue

        for w, dist in G[v].items():
            next_dist = current_dist + dist
            if distance[w] > next_dist:
                distance[w] = next_dist
                heappush(heap, (next_dist, w))

    return distance


input = sys.stdin.readline
INF = int(1e9)

T = int(input())
for _ in range(T):
    n, m ,t = map(int, input().split())             # n: 교차로(노드), m: 도로(간선), t: 목적지 후보 개수수
    s, g, h = map(int, input().split())             # s: 출발지, g, h: 중간에 거쳐간 교차로
    G = [{} for _ in range(n + 1)]                  # 간선 정보, G[v][w] : v -> w로 가는 비용
    for _ in range(m):
        a, b, d = map(int, input().split())         # 교차로 a, b, 비용 d
        G[a][b] = d
        G[b][a] = d

    end_list = [int(input()) for _ in range(t)]      # 목적지 후보(t개), 모두 s와 같지 않음

    distFrom_s = Dijkstra(n, s)
    if distFrom_s[g] > distFrom_s[h]:
        newS = g 
    elif distFrom_s[g] < distFrom_s[h]:
        newS = h
        
    distFrom_newS = Dijkstra(n, newS)
    result = []
    for end in end_list:
        if distFrom_s[newS] + distFrom_newS[end] == distFrom_s[end]:
            result.append(end)
    print(*sorted(result))