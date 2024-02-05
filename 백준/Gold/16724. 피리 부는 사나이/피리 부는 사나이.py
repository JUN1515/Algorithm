import sys
input = sys.stdin.readline

def find_parent(r, c):
    if parent[r][c] != (r, c):
        parent[r][c] = find_parent(*parent[r][c])
    return parent[r][c]


def union_parent(y1, x1, y2, x2):
    if depth[y1][x1] > depth[y2][x2]:
        parent[y1][x1] = parent[y2][x2]
        depth[y1][x1] = 1
    else:
        if depth[y1][x1] == depth[y2][x2]:
            depth[y1][x1] -= 1
        parent[y2][x2] = parent[y1][x1]
        depth[y2][x2] = 1


N, M = map(int, input().split())    # 행, 열
parent = [[(j, i) for i in range(M)] for j in range(N)]
depth = [[-1] * M for _ in range(N)]

arr = [list(input().strip()) for _ in range(N)]
direction = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

for r in range(N):
    for c in range(M):
        r1, c1 = find_parent(*parent[r][c])

        dr, dc = direction[arr[r][c]]
        nr, nc = r + dr, c + dc
        r2, c2 = find_parent(*parent[nr][nc])
        if (r1, c1) == (r2, c2): continue
        union_parent(r1, c1, r2, c2)

result = 0
for r in range(N):
    for c in range(M):
        if depth[r][c] != 1:
            result += 1
print(result)