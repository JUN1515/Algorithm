import sys
from heapq import *

def func(x):
    result = int(x) if x.isdigit() else int(1)
    return result


def Dijkstra(x1, y1, x2, y2):
    global N, M, arr
    INF = int(1e9)
    distance = [[INF] * M for _ in range(N)]
    distance[x1][y1] = 0

    heap = [(0, x1, y1)]
    heapify(heap)

    while heap:
        current_dist, r, c = heappop(heap)
        if distance[r][c] < current_dist: continue
        if r == x2 and c == y2:
            return current_dist

        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if nr < 0 or nr >= N or nc < 0 or nc >= M: continue
            next_dist = current_dist + 1 if arr[nr][nc] else current_dist
            if distance[nr][nc] > next_dist:
                distance[nr][nc] = next_dist
                heappush(heap, (next_dist, nr, nc))


input = sys.stdin.readline

N, M = map(int, input().split())    # 행 열
x1, y1, x2, y2 = map(int, input().split())  # x: 행, y: 열
arr = [list(map(func, input().strip())) for _ in range(N)]
print(Dijkstra(x1 - 1, y1 - 1, x2 - 1, y2 - 1))