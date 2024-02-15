import sys
input = sys.stdin.readline

def solution():

    def find_parent(x):
        if parent[x] < 0:
            return x
        parent[x] = find_parent(parent[x])
        return parent[x]

    def union_parent(x, y):
        if parent[x] > parent[y]:
            parent[x] = y
        else:
            if parent[x] == parent[y]:
                parent[x] -= 1
            parent[y] = x

    N, M, t = map(int, input().split())
    parent = [-1] * (N + 1)

    # A - B 사이 길 하나로 처리
    graph = [{} for _ in range(N + 1)]
    for _ in range(M):
        A, B, C = map(int, input().split())
        if A > B:
            A, B = B, A

        if B in graph[A]:
            if graph[A][B] <= C:
                continue
        graph[A][B] = C

    edges = []
    for a in range(1, N + 1):
        for b, c in graph[a].items():
            edges.append((a, b, c))
    edges.sort(key=lambda x: x[2])

    total_cost = 0
    cnt = 0
    for edge in edges:
        a, b, c = edge
        x, y = find_parent(a), find_parent(b)
        if x != y:
            union_parent(x, y)
            total_cost += c + (t * cnt)
            cnt += 1
    print(total_cost)


solution()