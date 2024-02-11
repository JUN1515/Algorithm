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

    N, M = map(int, input().split())    # N: 정점의 개수, M 간선의 개수
    parent = [-1] * (N + 1)

    edges = [list(map(int, input().split())) for _ in range(M)]
    edges.sort(key=lambda x: x[2])

    save_cost = 0

    for edge in edges:
        a, b, weight = edge
        save_cost += weight

        x1, y1 = find_parent(a), find_parent(b)
        if x1 != y1:
            union_parent(x1, y1)
            save_cost -= weight

    cnt = 0
    for i in range(1, N + 1):
        if parent[i] < 0:
            cnt += 1
            if cnt == 2:
                return -1
    return save_cost


print(solution())