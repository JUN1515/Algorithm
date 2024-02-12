import sys
input = sys.stdin.readline

def solution():

    def find_parent(x):
        if parent[x] != x:
            parent[x] = find_parent(parent[x])
        return parent[x]

    def union_parent(x, y):
        if x > y:
            parent[x] = y
        else:
            parent[y] = x

    N, M = map(int, input().split())
    parent = list(range(N + 1))
    universities = [""] + list(input().strip().split())

    edges = []
    for _ in range(M):
        u, v, d = map(int, input().strip().split())
        if universities[u] == universities[v]: continue
        edges.append((u, v, d))
    edges.sort(key=lambda x: x[2])

    result = 0
    for edge in edges:
        u, v, d = edge
        x, y = find_parent(u), find_parent(v)
        if x != y:
            union_parent(x, y)
            result += d

    cnt = 0
    for i in range(1, N + 1):
        if parent[i] == i:
            cnt += 1
            if cnt > 1:
                return -1

    return result


print(solution())