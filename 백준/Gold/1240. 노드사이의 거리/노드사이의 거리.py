from collections import deque

def solution():
    INF = int(1e9)
    N, M = map(int, input().split())

    graph = [{} for _ in range(N + 1)]
    for _ in range(N - 1):
        u, v, d = map(int, input().split())
        if graph[u].get(v, 0) != 0:
            if graph[u][v] >= d:
                continue
        graph[u][v] = d
        graph[v][u] = d

    arr = [[INF] * (N + 1) for _ in range(N + 1)]
    V = [0] * (N + 1)
    cnt = [0]

    answer = []
    for _ in range(M):
        a, b = map(int, input().split())
        if arr[a][b] == INF:
            bfs(a, graph, arr, V, cnt)
        answer.append(arr[a][b])

    for ans in answer:
        print(ans)

def bfs(s, graph, arr, V, cnt):
    cnt[0] += 1
    Q = deque([(0, s)])
    V[s] = cnt[0]
    while Q:
        current_dist, v = Q.popleft()
        for w, d in graph[v].items():
            if V[w] == cnt[0]: continue    # 방문한 경우
            next_dist = current_dist + d
            if arr[s][w] > next_dist:
                arr[s][w] = next_dist
                arr[w][s] = next_dist
            Q.append((next_dist, w))
            V[w] = cnt[0]


solution()