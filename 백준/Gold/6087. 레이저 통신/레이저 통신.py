import sys
from heapq import *

def find_C(W, H, arr):
    result = []
    count = 0
    for r in range(H):
        for c in range(W):
            if arr[r][c] == 'C':
                result.append((r, c))
                count += 1
                if count == 2:
                    return result


def Dijkstra(sr, sc, er, ec):
    global W, H, arr
    INF = int(1e9)
    direction = {1: (1, 0), 2: (-1, 0), 3: (0, 1), 4: (0, -1)}

    min_count = INF
    for d in range(1, 5):
        mirror_count = [[INF] * W for _ in range(H)]
        mirror_count[sr][sc] = 0

        heap = [(0, sr, sc, d)]   # 시작 비용, 시작 위치, 시작 방향
        heapify(heap)

        while heap:
            current_count, r, c, current_d = heappop(heap)
            if mirror_count[r][c] < current_count: continue
            if min_count <= current_count: break

            if r == er and c == ec:
                min_count = mirror_count[er][ec]
                break

            for next_d in range(1, 5):
                nr, nc = r + direction[next_d][0], c + direction[next_d][1]

                if nr < 0 or nr >= H or nc < 0 or nc >= W: continue
                if arr[nr][nc] == '*': continue

                next_count = current_count if current_d == next_d else current_count + 1
                if mirror_count[nr][nc] > next_count:
                    mirror_count[nr][nc] = next_count
                    heappush(heap, (next_count, nr, nc, next_d))

    return min_count


input = sys.stdin.readline

W, H = map(int, input().split())    # 열, 행
arr = [list(input().strip()) for _ in range(H)]

C_list = find_C(W, H, arr)
r1, c1 = C_list[0]
r2, c2 = C_list[1]

print(Dijkstra(r1, c1, r2, c2))