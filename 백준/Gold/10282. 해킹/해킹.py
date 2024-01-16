import sys
from heapq import *

def Dijkstra(N, start):
    global INF, G
    time = [INF] * (N + 1)
    time[start] = 0

    heap = [(0, start)]
    heapify(heap)

    while heap:
        current_time, v = heappop(heap)
        if time[v] < current_time: continue

        for w, t in G[v].items():
            next_time = current_time + t
            if time[w] > next_time:
                time[w] = next_time
                heappush(heap, (next_time, w))

    count = max_time = 0
    for i in range(1, N + 1):
        if time[i] != INF:
            count += 1
            max_time = max(max_time, time[i])
    return  count, max_time


input = sys.stdin.readline
T = int(input())
INF = int(1e10)

for _ in range(T):
    # n: 컴퓨터 개수(정점의 개수), d: 의존성 개수(간선의 개수), c: 컴퓨터 번호(시작점)
    n, d, c = map(int, input().split())

    # 간선 정보 (단방향) b -> a
    G = [{} for _ in range(n + 1)]
    for _ in range(d):
        # b -> a 감염 시간 s초
        a, b, s = map(int, input().split())
        G[b][a] = s

    print(*Dijkstra(n, c))