import sys
from heapq import *

def find_door():
    global N, arr, door
    count = 0
    for r in range(N):
        for c in range(N):
            if arr[r][c] == '#':
                count += 1
                door.append((r, c))
                if count == 2:
                    return

def Dijkstra(sr, sc, er, ec):
    global N, arr, door

    INF = int(2500)
    direction = {1: (1, 0), 2: (-1, 0), 3: (0, 1), 4: (0, -1)}

    min_count = INF

    for d in range(1, 5):
        mirror_count = [[INF] * N for _ in range(N)]
        mirror_count[sr][sc] = 0

        heap = [(0, sr, sc, d)] # 시작시 비용, 시작 위치(r, c), 시작 방향
        heapify(heap)

        while heap:
            current_count, r, c, d = heappop(heap)

            if mirror_count[r][c] < current_count: continue
            if min_count <= current_count: break

            if r == er and c == ec:
                min_count = current_count
                break

            nr, nc = r + direction[d][0], c + direction[d][1]
            if nr < 0 or nr >= N or nc < 0 or nc >= N: continue

            while True:
                if arr[nr][nc] == '*':
                    break

                elif arr[nr][nc] == '!':
                    next_count = current_count + 1
                    if mirror_count[nr][nc] > next_count:
                        mirror_count[nr][nc] = next_count
                        d_list = [3, 4] if d <= 2 else [1, 2]
                        for nd in d_list:
                            heappush(heap, (next_count, nr, nc, nd))

                elif arr[nr][nc] == '#':
                    heappush(heap, (current_count, nr, nc, d))
                    break

                nr, nc = nr + direction[d][0], nc + direction[d][1]
                if nr < 0 or nr >= N or nc < 0 or nc >= N: break

    return min_count

input = sys.stdin.readline

# 집의 크기
N = int(input())
arr = [list(input().strip()) for _ in range(N)]
door = []
find_door()

result = Dijkstra(*door[0], *door[1])
print(result)