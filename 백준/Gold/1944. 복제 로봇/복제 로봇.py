import sys
from collections import deque
input = sys.stdin.readline

def bfs(N, M, nodes, arr):
    path = [[0] * (M + 1) for _ in range(M + 1)]        # path[i][j]는 i -> j 이동 비용
    visited = [[0] * N for _ in range(N)]
    distance = [[0] * N for _ in range(N)]

    for start in nodes:
        sr, sc, node = start

        Q = deque([(sr, sc)])
        visited[sr][sc] = node
        distance[sr][sc] = 1

        while Q:
            r, c = Q.popleft()

            if arr[r][c] > 0 and arr[r][c] != node:         # 열쇠가 있는 곳이고, 출발한 노드가 다른 경우
                i, j = (node - 1, arr[r][c] - 1) if node < arr[r][c] else (arr[r][c] - 1, node - 1)
                if path[i][j] == 0 or path[i][j] > distance[r][c] - 1:
                    path[i][j] = distance[r][c] - 1

            for dr, dc in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                nr, nc = r + dr, c + dc
                if arr[nr][nc] == -1: continue      # 벽이라면 무시
                if visited[nr][nc] == node:         # 방문한 적이 있는 경우
                    if distance[nr][nc] <= distance[r][c] + 1:
                        continue                    # 다음 경로의 값이 더 작거나 같은 경우 패스

                Q.append((nr, nc))
                visited[nr][nc] = node
                distance[nr][nc] = distance[r][c] + 1

    graph = []
    for i in range(M):
        for j in range(i + 1, M + 1):
            if path[i][j] == 0: continue
            graph.append((i, j, path[i][j]))

    return graph


def find_parent(x, parent):
    if parent[x] < 0:
        return x
    parent[x] = find_parent(parent[x], parent)
    return parent[x]


def union_parent(x, y, parent):
    if parent[x] > parent[y]:
        parent[x] = y
    else:
        if parent[x] == parent[y]:
            parent[x] -= 1
        parent[y] = x


def solution():
    N, M = map(int, input().split())
    parent = [-1] * (M + 1)

    arr = [(list(input().strip())) for _ in range(N)]
    nodes = []
    cnt = 1
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '1':
                arr[i][j] = -1
            elif arr[i][j] == '0':
                arr[i][j] = 0
            else:
                nodes.append((i, j, cnt))
                arr[i][j] = cnt
                cnt += 1

    edges = bfs(N, M, nodes, arr)
    if edges == []:
        return -1

    edges.sort(key=lambda x: x[2])

    result = 0
    for edge in edges:
        a, b, w = edge
        x, y = find_parent(a, parent), find_parent(b, parent)

        if x != y:
            union_parent(x, y, parent)
            result += w

    # 모든 열쇠 찾았는지 확인
    r_cnt = 0
    for i in parent:
        if i < 0:
            r_cnt += 1
            if r_cnt == 2:
                return -1

    return result


print(solution())