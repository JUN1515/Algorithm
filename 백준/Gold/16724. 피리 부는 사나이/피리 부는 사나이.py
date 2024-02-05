import sys
input = sys.stdin.readline

def delta(r, c, cnt):
    global arr, visited

    while True:
        visited[r][c] = cnt

        dr, dc = direction[arr[r][c]]
        nr, nc = r + dr, c + dc

        if not visited[nr][nc]:
            r, c = nr, nc

        else:
            if visited[r][c] == visited[nr][nc]:
                return 1
            return 0


N, M = map(int, input().split())    # 행, 열

arr = [list(input().strip()) for _ in range(N)]
direction = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

visited = [[0] * M for _ in range(N)]

num = 1
result = 0
for row in range(N):
    for col in range(M):
        if not visited[row][col]:
            result += delta(row, col, num)
            num += 1
print(result)