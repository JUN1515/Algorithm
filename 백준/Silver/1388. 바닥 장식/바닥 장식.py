def dfs_row(r, c):
    global N, M
    arr[r][c] = '.'
    S = [(r, c)]

    while S:
        r, c = S.pop()

        for dc in (-1, 1):
            nc = c + dc
            if nc < 0 or nc >= M: continue
            if arr[r][nc] == '-':
                arr[r][nc] = '.'
                S.append((r, nc))

def dfs_col(r, c):
    global N, M
    arr[r][c] = '.'
    S = [(r, c)]

    while S:
        r, c = S.pop()

        for dr in (-1, 1):
            nr = r + dr
            if nr < 0 or nr >= N: continue
            if arr[nr][c] == '|':
                arr[nr][c] = '.'
                S.append((nr, c))


N, M = map(int, input().strip().split())    # 행, 열
arr = [list(input()) for _ in range(N)]

cnt = 0
for r in range(N):
    for c in range(M):
        if arr[r][c] == '-':
            dfs_row(r, c)
            cnt += 1
        elif arr[r][c]  == '|':
            dfs_col(r, c)
            cnt += 1
print(cnt)
