import sys
from heapq import *
input = sys.stdin.readline

def bfs(N, M, start, arr):
    INF = 2500
    visited = [[INF] * N for _ in range(N)]
    sr, sc = start

    result = 0
    Q = [(0, sr, sc)]
    while Q:
        cureent_dist, r, c = heappop(Q)

        if arr[r][c] == 'K':
            if visited[r][c] == INF:
                visited[r][c] = cureent_dist
                result += cureent_dist
                M -= 1
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc
                    if arr[nr][nc] == '1': continue
                    if visited[nr][nc] > 1:
                        heappush(Q, (1, nr, nc))
            continue

        if visited[r][c] > cureent_dist:
            visited[r][c] = cureent_dist
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if arr[nr][nc] == '1': continue
                heappush(Q, (cureent_dist + 1, nr, nc))

    if M:
        return -1
    else:
        return result


def solution():
    N, M = map(int, input().split())
    arr = [(list(input().strip())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'S':
                answer = bfs(N, M, (i, j), arr)
                return answer


print(solution())