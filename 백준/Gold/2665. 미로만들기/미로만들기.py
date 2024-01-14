import sys
from heapq import *

def Dijstra(N, arr):
    INF = 1e9
    count = [[INF] * N for _ in range(N)]

    heap = [(0, 0, 0)]  # 시작시 비용, 시작 좌표 행, 열
    heapify(heap)

    while heap:
        current_count, r, c = heappop(heap)

        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if count[r][c] < current_count: continue

        # 만약 끝 점에 도착하면 return
        if r == c == N - 1:
            return current_count

        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for dr, dc in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            nr, nc = r + dr, c + dc
            if nr < 0 or nr >= N or nc < 0 or nc >= N: continue

            # 만약 흰 방이면 count를 세지 않고, 검은 방이면 count를 1 센다.
            next_count = current_count + 0 if arr[nr][nc] else current_count + 1
            if count[nr][nc] > next_count:
                count[nr][nc] = next_count
                heappush(heap, (next_count, nr, nc))

input = sys.stdin.readline

n = int(input())
arr = [[int(x) for x in input() if x != "\n"] for _ in range(n)]
result = Dijstra(n, arr)
print(result)